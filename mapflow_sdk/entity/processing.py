from typing import Optional, Union
from pydantic import BaseModel
from enum import Enum
from pydantic_geojson import PolygonModel, MultiPolygonModel

from .enums import ProcessingStatus
from .model import Model


class Rating(int, Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class RasterLayer(BaseModel):
    id: str
    tileJsonUrl: str
    tileUrl: str


class UserFeedback(BaseModel):
    rating: Rating
    feedback: Optional[str]


class Processing(BaseModel):
    id: str
    name: str
    projectId: str
    workflowDef: Model
    aoiCount: int
    aoiArea: int
    area: int
    cost: int
    status: ProcessingStatus
    description: Optional[str]
    rasterLayer: Optional[RasterLayer]
    rating: Optional[UserFeedback]

# ==== POST ==== #


class SourceType(str, Enum):
    xyz = 'xyz'
    tms = 'tms'
    quadkey = 'quadkey'
    sentinel_l2a = 'sentinel_l2a'


class CRS(str, Enum):
    web_mercator = 'epsg:3857'
    world_mercator = 'epsg:3395'


class ProviderName(BaseModel):
    data_provider: str


class ProviderParams(BaseModel):
    url: str
    source_type: Optional[SourceType]
    projection: Optional[CRS]


class PostProcessingSchema(BaseModel):
    name: str
    geometry: Union[PolygonModel, MultiPolygonModel]
    wdId: str
    params: Union[ProviderParams, ProviderName]
    meta: dict
