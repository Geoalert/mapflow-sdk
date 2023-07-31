import json


def save(filename, data):
    """
    To save the processing results
    Currently operates only with geojson files
    """
    with open(filename, "w") as dst:
        dst.write(json.dumps(data))


def load(filename):
    """
    To load previously saved processing results
    Currently operates only with geojson files
    """
    with open(filename) as src:
        return json.load(src)


def load_aoi(filename):
    """
    To load AOI for processing. Gets the first geometry from file, discarding everything else
    If the file is corrupted, raises ValueError
    Currently operates only with geojson files
    """
    featurecollection = load(filename)
    try:
        features = featurecollection['features']
        aoi = features[0]['geometry']
    except KeyError:
        raise ValueError("File is corrupted: geojson must contain `features` key,"
                         " and feature must contain `geometry` key")
    except IndexError:
        raise ValueError("File does not contain any features!")
    return aoi