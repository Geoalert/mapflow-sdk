from pydantic import BaseModel
from typing import List, Optional

from .model import Model


class Project(BaseModel):
    id: str
    name: str
    description: Optional[str]
    isDefault: bool
    created: str
    updated: str
    workflowDefs: List[Model]
