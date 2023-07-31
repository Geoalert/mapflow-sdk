# Mapflow SDK

Python library for easy acceess to [Mapflow API](https://docs.mapflow.ai/api/mapflow_api.html).

# You can find it useful, if
- If you are a GIS researchers, you can use it in Jupyter notebooks or scripts
- If you are a Python developer and want to access Mapflow API from your application

You can use Mapflow API directly, but this SDK provides easier access from your Python code.

# Requirements

- Python 3.8+
- python-requests
- registration at [Mapflow.ai](https://mapflow.ai)

# Installation

`pip install mapflow-sdk`

# Obtain API token
 Visit [account/API section](https://dev.mapflow.ai/account/api) and get token to use it with API
 
# Basic usage
See example
```bash
cd example
python3 example.py <YOUR_MAPFLOW_TOKEN>
```

The example will create file `output.geojson`