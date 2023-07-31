from pydantic import BaseModel
from typing import Optional, Any


class Model(BaseModel):
    id: str
    name: str
    description: str = ""
    pricePerSqKm: float = 1.0
    created: str = ""
    updated: str = ""
    blocks: Optional[Any] = None
