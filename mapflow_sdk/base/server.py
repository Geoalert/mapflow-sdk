import requests
from typing import Optional
from urllib.parse import urljoin
url = "https://api.mapflow.ai/rest/"
mapflow_token = ""


# The token is stored in the module global so that the user would not need to pass the token to each request
def login(token: str):
    # Try to get a resoponse to make sure the token is valid. Only in case of success, the token will be saved
    response = requests.get(url=mapflow_url("user/status"),
                            headers=auth_header(token))
    if response.status_code in [401, 403]:
        raise ValueError("Login failed! Invalid Mapflow token. "
                         "Please visit https://mapflow.ai/account/api to get a new one")
    elif response.status_code != 200:
        response.raise_for_status()
    else:
        global mapflow_token
        mapflow_token = token


def auth_header(token: Optional[str] = None):
    if token is None:
        token = mapflow_token
    return {"Authorization": f"Basic {token}"}


def mapflow_url(postfix: str):
    return urljoin(url, postfix)


def get_json(postfix: str,
             token: Optional[str] = None):
    response = requests.get(url=mapflow_url(postfix),
                            headers=auth_header(token))
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()


def post_json(postfix: str,
              json: dict,
              token: Optional[str] = None):
    response = requests.post(url=mapflow_url(postfix=postfix),
                             json=json,
                             headers=auth_header(token))
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()