from typing import Optional, Union
from pydantic import BaseModel
from enum import Enum
from pydantic_geojson import PolygonModel, MultiPolygonModel
from .model import ModelSchema


class ProcessingStatus(str, Enum):
    OK = "OK"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    UNPROCESSED = "UNPROCESSED"


class Rating(int, Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class RasterLayerSchema(BaseModel):
    id: str
    tileJsonUrl: str
    tileUrl: str


class RatingSchema(BaseModel):
    rating: Rating
    feedback: Optional[str]


class ProcessingSchema(BaseModel):
    id: str
    name: str
    projectId: str
    workflowDef: ModelSchema
    aoiCount: int
    aoiArea: int
    area: int
    cost: int
    status: ProcessingStatus
    description: Optional[str]
    rasterLayer: Optional[RasterLayerSchema]
    rating: Optional[RatingSchema]

# ==== POST ==== #


class SourceType(str, Enum):
    xyz = 'xyz'
    tms = 'tms'
    quadkey = 'quadkey'
    sentinel_l2a = 'sentinel_l2a'


class CRS(str, Enum):
    web_mercator = 'epsg:3857'
    world_mercator = 'epsg:3395'


class ProviderNameSchema(BaseModel):
    data_provider: str


class ProviderParamsSchema(BaseModel):
    url: str
    source_type: Optional[SourceType]
    projection: Optional[CRS]


class PostProcessingSchema(BaseModel):
    name: str
    geometry: Union[PolygonModel, MultiPolygonModel]
    wdId: str
    params: Union[ProviderParamsSchema, ProviderNameSchema]
    meta: dict
