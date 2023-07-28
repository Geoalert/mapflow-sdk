from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

from .model import ModelSchema
from .provider import ProviderSchema


class BillingType(str, Enum):
    CREDITS = "CREDITS"
    NONE = "NONE"
    AREA = "AREA"


class UserSchema(BaseModel):
    email: str
    billingType: BillingType
    models: List[ModelSchema]
    remainingCredits: int = None
    dataProviders: Optional[List[ProviderSchema]] = None
    processedArea: Optional[int] = None
    remainingArea: Optional[int] = None
    memoryLimit: Optional[int] = None
    areaLimit: Optional[int] = None
    maxAoisPerProcessing: Optional[int] = None
