from typing import Optional
from ..base import server
from ..entity import User


def status(token: Optional[str] = None):
    response = server.get_json(postfix='user/status',
                               token=token)
    return User(**response)
