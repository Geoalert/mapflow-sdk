from typing import Optional, List
from pydantic import BaseModel
from enum import Enum

from .model import Model
from .provider import Provider


class BillingType(str, Enum):
    CREDITS = "CREDITS"
    NONE = "NONE"
    AREA = "AREA"


class User(BaseModel):
    email: str
    billingType: BillingType
    models: List[Model]
    remainingCredits: int = None
    dataProviders: Optional[List[Provider]] = None
    processedArea: Optional[int] = None
    remainingArea: Optional[int] = None
    memoryLimit: Optional[int] = None
    areaLimit: Optional[int] = None
    maxAoisPerProcessing: Optional[int] = None
