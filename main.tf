# EventBridge Rule
resource "aws_cloudwatch_event_rule" "eb_pipeline" {
  name                = "pipeline_test"
  schedule_expression = "rate(1 minute)"
}

data "aws_iam_policy_document" "eventbridge_policy" {
  statement {
    actions = [
      "events:DescribeRule",
      "events:PutRule",
      "events:ListRules",
      "states:ListStateMachines",
      "states:DescribeStateMachine",
      "states:StartExecution"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role" "event_bridge_role" {
  name = "event-bridge-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "events.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "eventbridge_policy" {
  name        = "EventBridgePolicy"
  description = "Policy for EventBridge to invoke resources"
  policy      = data.aws_iam_policy_document.eventbridge_policy.json
}

resource "aws_iam_role_policy_attachment" "eventbridge_policy_attachment" {
  role       = aws_iam_role.event_bridge_role.name
  policy_arn = aws_iam_policy.eventbridge_policy.arn
}


data "aws_sfn_state_machine" "existing_state_machine" {
  name = "MyStateMachine"
}

resource "aws_cloudwatch_event_target" "sfn_target" {
  rule      = aws_cloudwatch_event_rule.eb_pipeline.name
  arn       = data.aws_sfn_state_machine.existing_state_machine.arn
  role_arn  = aws_iam_role.event_bridge_role.arn
  input     = jsonencode(
    {
      "items": [
        {
          "item": "test_item1"
        },
        {
          "item": "empty"
        },
        {
          "item": "test_item2"
        }
      ]
    }
  )
}
