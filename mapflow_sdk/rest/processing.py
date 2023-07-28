from typing import Optional, Union
from ..schema import ProcessingSchema, AoiSchema, PostProcessingSchema
from ..schema.processing import SourceType, CRS, ProviderParamsSchema, ProviderNameSchema
from ..base import server, object_or_id
from .. import __version__


def get_processing(processing_id: str,
                   token: str):
    response = server.get_json(f'processings/{processing_id}', token)
    return ProcessingSchema(**response)


def get_processing_result(processing: Union[ProcessingSchema, str],
                          token: str):
    """
    Specify either processing_id or processing (ProcessingSchema). If
    """
    processing_id = object_or_id(processing, ProcessingSchema)
    response = server.get_json(postfix=f"processings/{processing_id}/result", token=token)
    return response


def get_processing_aois(processing: Union[ProcessingSchema, str],
                        token: str):
    processing_id = object_or_id(processing, ProcessingSchema)
    response = server.get_json(postfix=f"processings/{processing_id}/aois", token=token)
    return [AoiSchema(**entity) for entity in response]


def post_processing(name: str,
                    geometry: dict,
                    wd_id: str,
                    url: Optional[str] = None,
                    source_type: SourceType = SourceType.xyz,
                    projection: CRS = CRS.web_mercator,
                    provider_name: Optional[str] =  None,
                    meta: Optional[dict] = None,
                    token: str = ""):
    if provider_name:
        provider = ProviderNameSchema(data_provider=provider_name)
    elif url:
        provider = ProviderParamsSchema(url=url,
                                        source_typse=source_type,
                                        projection=projection)
    else:
        raise ValueError("Provider name or url must be specified")

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

    return ProcessingSchema(**response)