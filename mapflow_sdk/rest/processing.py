from typing import Optional, Union

from ..entity import Processing, Aoi, PostProcessingSchema
from ..entity.processing import SourceType, CRS, ProviderParams, ProviderName
from ..base import server, object_or_id
from .. import __version__


def get(processing_id: str,
        token: Optional[str] = None):
    response = server.get_json(f'processings/{processing_id}', token)
    return Processing(**response)


def result(processing: Union[Processing, str],
           token: Optional[str] = None):
    """
    Specify either processing_id or processing (ProcessingSchema). If
    """
    processing_id = object_or_id(processing, Processing)
    response = server.get_json(postfix=f"processings/{processing_id}/result", token=token)
    return response


def aois(processing: Union[Processing, str],
         token: Optional[str] = None):
    processing_id = object_or_id(processing, Processing)
    response = server.get_json(postfix=f"processings/{processing_id}/aois", token=token)
    return [Aoi(**entity) for entity in response]


def start(name: str,
          geometry: dict,
          wd_id: str,
          url: Optional[str] = None,
          source_type: SourceType = SourceType.xyz,
          projection: CRS = CRS.web_mercator,
          provider_name: Optional[str] = None,
          meta: Optional[dict] = None,
          token: Optional[str] = None):
    if provider_name:
        provider = ProviderName(data_provider=provider_name)
    elif url:
        provider = ProviderParams(url=url,
                                  source_typse=source_type,
                                  projection=projection)
    else:
        raise ValueError("Provider name or url must be specified")

    # SDK sends information of the version for the server to understand the caller's interface
    sdk_meta = {"source-app": "mapflow-sdk", "version": __version__}
    if not meta:
        meta = sdk_meta
    else:
        meta.update(sdk_meta)

    processing = PostProcessingSchema(name=name,
                                      geometry=geometry,
                                      wdId=wd_id,
                                      params=provider,
                                      meta=meta
                                      )

    response = server.post_json(postfix="processings",
                                json=processing.model_dump(),
                                token=token)

    return Processing(**response)
