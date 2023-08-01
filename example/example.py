import sys
import time
import mapflow_sdk as mf


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: `python3 example.py <YOUR MAPFLOW TOKEN>. Exitinig")
        exit()
    token = sys.argv[1]
    # Login (save your token for further use)
    mf.login(token)
    # Get user info
    userinfo = mf.user.status()

    default_project = mf.project.default()
    # Select the first model (workflow def)
    model = default_project.workflowDefs[0]
    wdid = model.id
    # Select the first data provider
    provider = userinfo.dataProviders[1]
    providername = provider.name
    print(f"Selected model `{model.name}` and provider `{provider.displayName}`")
    # load AOI
    aoi = mf.vector.load_aoi("aoi.geojson")
    # Starting new processing
    print("Starting processing")
    try:
        processing = mf.processing.start(name="MyAwesomeProcessing",
                                         geometry=aoi,
                                         wd_id=wdid,
                                         provider_name=providername,
                                         token=token)
    except Exception as e:
        print (f"Error while starting processing: {e}")
        exit(1)
    else:
        print(f"Processing {processing.name} sucessfully started with id {processing.id}. "
              f"Waiting for the processing to finish.")
    while True:
        print(".")
        time.sleep(10)
        processing = mf.processing.get(processing.id)
        if processing.status != mf.ProcessingStatus.IN_PROGRESS:
            print("Processing finished!")
            break
    # Download the results
    result = mf.processing.result(processing=processing, token=token)
    # Save to file
    mf.vector.save("output.geojson", result)
