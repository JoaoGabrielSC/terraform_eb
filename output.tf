# Outputs

output "event_rule_arn" {
  value = aws_cloudwatch_event_rule.eb_pipeline.arn
}

output "event_rule_name" {
  value = aws_cloudwatch_event_rule.eb_pipeline.name
}
