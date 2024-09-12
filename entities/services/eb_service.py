import boto3
from entities.config import Config, EnvVars, EventRuleResponse

def enable_event_rule() -> EventRuleResponse:
    print("=== ENABLING EVENT RULE ===")
    eventbus_name = Config().get(EnvVars.EVENT_BUS_NAME.value)
    client = boto3.client(
        'events',
        region_name = Config().get(EnvVars.AWS_DEFAULT_REGION.value),
        aws_access_key_id = Config().get(EnvVars.AWS_ACCESS_KEY_ID.value),
        aws_secret_access_key = Config().get(EnvVars.AWS_SECRET_ACCESS_KEY.value)
    )
    
    rule_details = client.describe_rule(Name=eventbus_name)

    response = client.put_rule(
        Name=eventbus_name,
        EventPattern=rule_details.get('EventPattern', ''),
        ScheduleExpression=rule_details.get('ScheduleExpression', ''),
        State='ENABLED'
    )
    
    return EventRuleResponse(
        RuleArn=response['RuleArn'],
        Name=response['Name'],
        State=response['State'],
        ScheduleExpression=response.get('ScheduleExpression', None),
        EventPattern=response.get('EventPattern', None)
    )

def disable_event_rule()-> dict:
    print("=== DISABLING EVENT RULE ===")
    eventbus_name = Config().get(EnvVars.EVENT_BUS_NAME.value)
    client = boto3.client(
        'events',
        region_name = Config().get(EnvVars.AWS_DEFAULT_REGION.value),
        aws_access_key_id = Config().get(EnvVars.AWS_ACCESS_KEY_ID.value),
        aws_secret_access_key = Config().get(EnvVars.AWS_SECRET_ACCESS_KEY.value)
    )
    
    rule_details = client.describe_rule(Name=eventbus_name)
    response = client.put_rule(
        Name=eventbus_name,
        EventPattern=rule_details.get('EventPattern', ''),
        ScheduleExpression=rule_details.get('ScheduleExpression', ''),
        State='DISABLED'
    )
    
    return EventRuleResponse(
        RuleArn=response['RuleArn'],
        Name=response['Name'],
        State=response['State'],
        ScheduleExpression=response.get('ScheduleExpression', None),
        EventPattern=response.get('EventPattern', None)
    )
