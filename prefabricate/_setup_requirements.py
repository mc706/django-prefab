import pip


def setup_requirements(blueprint):
    dependencies = blueprint.get('dependencies', [])
    if blueprint.get('django_version', False):
        dependencies.push({
            "name": "django",
            "version": blueprint.get('django_verison')
        })
    if blueprint.get('environment', {}).get('fabric', False) and blueprint.get('environment', {}).get('fabric', {}).get(
            'use', True):
        dependencies.push({"name": "fabric"})
    if blueprint.get('environment', {}).get('coverage', False) and blueprint.get('environment', {}).get('coverage',
            {}).get('use', True):
        dependencies.push({"name": "coverage"})
    for package in dependencies:
        package_name = package.get('name')
        if package.get('version', ''):
            package_name += "==" + package.get('version')
        pip.main(['install', package_name])