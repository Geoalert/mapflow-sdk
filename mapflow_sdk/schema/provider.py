from pydantic import BaseModel
from typing import List, Dict


class ProviderSchema(BaseModel):
    id: str
    name: str
    displayName: str
    price: List[Dict]
