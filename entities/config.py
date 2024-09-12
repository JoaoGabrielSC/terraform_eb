import os
from enum import Enum
from typing import Optional
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

class EnvVars(Enum):
    AWS_ACCESS_KEY_ID='AWS_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY='AWS_SECRET_ACCESS_KEY'
    AWS_DEFAULT_REGION='AWS_DEFAULT_REGION'
    EVENT_BUS_NAME='EVENT_BUS_NAME'


@dataclass
class EventRuleResponse:
    RuleArn: str
    Name: str
    State: str
    ScheduleExpression: Optional[str] = None
    EventPattern: Optional[str] = None

@dataclass
class APIResponse:
    status_code: str
    response: Optional[EventRuleResponse] = None
    error: Optional[str] = None

class Config:

    __instance = None # singleton instance
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.config = {}
            for var in EnvVars:
                try:
                    cls.__instance.config[var.value] = os.environ[var.value]
                except KeyError:
                    print(f"Warning: Environment Variable '{var.value} not defined")
        return cls.__instance

    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            return None
