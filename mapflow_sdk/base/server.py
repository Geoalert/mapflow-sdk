import requests
from urllib.parse import urljoin
url = "https://api.mapflow.ai/rest/"


def auth_header(token: str):
    return {"Authorization": f"Basic {token}"}


def mapflow_url(postfix: str):
    return urljoin(url, postfix)


def get_json(postfix: str,
             token: str):
    response = requests.get(url=mapflow_url(postfix),
                            headers=auth_header(token))
    if response.status_code != 200:
        response.raise_for_status()
    print(response.text)
    return response.json()


def post_json(postfix: str,
              json: dict,
              token: str):
    response = requests.post(url=mapflow_url(postfix=postfix),
                             json=json,
                             headers=auth_header(token))
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()
