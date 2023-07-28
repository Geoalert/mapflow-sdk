from ..schema import ProjectSchema, ProcessingSchema
from ..base import server


def get_projects(token: str):
    response = server.get_json('projects', token)
    return [ProjectSchema(**entry) for entry in response]


def get_default_project(token: str):
    response = server.get_json('projects/default', token)
    return ProjectSchema(**response)


def get_project(project_id: str,
                token: str):
    response = server.get_json(f'projects/{project_id}', token)
    return ProjectSchema(**response)


def get_project_processings(project_id: str,
                            token: str):
    response = server.get_json(postfix=f'projects/{project_id}/processings',
                               token=token)
    return [ProcessingSchema(**entry) for entry in response]
