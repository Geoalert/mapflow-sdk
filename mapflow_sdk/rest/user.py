from ..base import server
from mapflow_sdk.schema import UserSchema


def get_user(token):
    response = server.get_json(postfix='user/status',
                               token=token)
    return UserSchema(**response)
