from django.core import management

from _exceptions import ProjectNameRequired


def start_project(blueprint):
    if not blueprint.get('project_name', False):
        raise ProjectNameRequired
    else:
        management.call_command('startproject', blueprint.get('project_name'))
    return True