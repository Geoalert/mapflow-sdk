import time
from mapflow_sdk import (get_user,
                         get_default_project,
                         get_processing,
                         get_processing_result,
                         post_processing)
from mapflow_sdk.io import save_result
from mapflow_sdk.schema.processing import ProcessingStatus

token = "<YOUR TOKEN>"

if __name__ == "__main__":
    # get userinfo
    userinfo = get_user(token)

    default_project = get_default_project(token)
    wdid = default_project.workflowDefs[0].id
    providername = userinfo.dataProviders[0].name

    processing = post_processing(name="MyAwesomeProcessing",
                                 geometry={"coordinates": [[[37.68238571296315, 55.672002849416224],
                                                            [37.68995100104415, 55.672002849416224],
                                                            [37.68995100104415, 55.67564915875106],
                                                            [37.68238571296315, 55.67564915875106],
                                                            [37.68238571296315, 55.672002849416224]]],
                                           "type": "Polygon"},
                                 wd_id=wdid,
                                 provider_name=providername,
                                 token=token)
    while True:
        time.sleep(60)
        processing = get_processing(processing.id)
        if processing.status != ProcessingStatus.IN_PROGRESS:
            print("processing finished!")
            break

    result = get_processing_result(processing=processing, token=token)
    save_result("result.geojson", result)