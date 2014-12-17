from fabric.api import local

from _exceptions import ProjectNameRequired


def _setup_virutalenv(name):
    # TODO: use fabenv instead
    return local('mkvirtualenv %s' % name)


def setup_environment(blueprint):
    # setup virtual environment
    if 'virtualenv' in blueprint.get('environment', {}) and blueprint.get('environment', {}).get('virtualenv', {}).get(
            'use', True):
        if not blueprint.get('environment', {}).get('virtualenv', {}).get('name', "") and not blueprint.get(
                'project_name'):
            raise ProjectNameRequired
        else:
            name = blueprint.get('environment', {}).get('virtualenv', {}).get('name', blueprint.get('project_name'))
        _setup_virutalenv(name)

        #setup