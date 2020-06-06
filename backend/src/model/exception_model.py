from enum import Enum
from pydantic import BaseModel


class ErrorRequestConfigValidationEnum(str, Enum):
    INVALID_ENV = 'INVALID_ENVIRONMENT',
