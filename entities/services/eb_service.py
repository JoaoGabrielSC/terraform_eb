import boto3
from entities.config import Config, EnvVars

def enable_event_rule():
    print("=== ENABLING EVENT RULE ===")
    eventbus_name = Config().get(EnvVars.EVENT_BUS_NAME.value)
    client = boto3.client(
        'events',
        region_name = Config().get(EnvVars.AWS_DEFAULT_REGION.value),
        aws_access_key_id = Config().get(EnvVars.AWS_ACCESS_KEY_ID.value),
        aws_secret_access_key = Config().get(EnvVars.AWS_SECRET_ACCESS_KEY.value)
    )
    
    # Fetch existing rule details to get the pattern or expression
    rule_details = client.describe_rule(Name=eventbus_name)
    # print(rule_details)
    response = client.put_rule(
        Name=eventbus_name,
        EventPattern=rule_details.get('EventPattern', ''),
        ScheduleExpression=rule_details.get('ScheduleExpression', ''),
        State='ENABLED'
    )
    
    return response

def disable_event_rule():
    print("=== DISABLING EVENT RULE ===")
    eventbus_name = Config().get(EnvVars.EVENT_BUS_NAME.value)
    client = boto3.client(
        'events',
        region_name = Config().get(EnvVars.AWS_DEFAULT_REGION.value),
        aws_access_key_id = Config().get(EnvVars.AWS_ACCESS_KEY_ID.value),
        aws_secret_access_key = Config().get(EnvVars.AWS_SECRET_ACCESS_KEY.value)
    )
    
    # Fetch existing rule details to get the pattern or expression
    rule_details = client.describe_rule(Name=eventbus_name)
    # print(rule_details)
    response = client.put_rule(
        Name=eventbus_name,
        EventPattern=rule_details.get('EventPattern', ''),
        ScheduleExpression=rule_details.get('ScheduleExpression', ''),
        State='DISABLED'
    )
    
    return response
