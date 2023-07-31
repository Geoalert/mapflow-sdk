from pydantic import BaseModel
from pydantic_geojson import PolygonModel, MultiPolygonModel
from typing import List, Union
from .enums import ProcessingStatus
from .error_message import ErrorMessage


class Aoi(BaseModel):
    id: str
    status: ProcessingStatus
    percentCompleted: int
    geometry: Union[PolygonModel, MultiPolygonModel]
    area: int
    messages: List[ErrorMessage]
