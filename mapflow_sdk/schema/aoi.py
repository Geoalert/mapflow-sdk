from pydantic import BaseModel
from pydantic_geojson import PolygonModel, MultiPolygonModel
from typing import List, Union
from .processing import ProcessingStatus
from .error_message import ErrorMessageSchema


class AoiSchema(BaseModel):
    id: str
    status: ProcessingStatus
    percentCompleted: int
    geometry: Union[PolygonModel, MultiPolygonModel]
    area: int
    messages: List[ErrorMessageSchema]
