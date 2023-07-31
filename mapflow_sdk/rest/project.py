from typing import Optional
from ..entity import Project, Processing
from ..base import server


def all_projects(token: Optional[str] = None):
    response = server.get_json('projects', token)
    return [Project(**entry) for entry in response]


def default(token: Optional[str]=None):
    response = server.get_json('projects/default', token)
    return Project(**response)


def get(project_id: str,
        token: Optional[str] = None):
    response = server.get_json(f'projects/{project_id}', token)
    return Project(**response)


def processings(project_id: str,
                token: Optional[str] = None):
    response = server.get_json(postfix=f'projects/{project_id}/processings',
                               token=token)
    return [Processing(**entry) for entry in response]
