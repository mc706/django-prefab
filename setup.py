from setuptools import setup

import re
VERSIONFILE="prefabricate/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
    major, minor, patch = verstr.split('.')
    release = "%s.%s" %(major, minor)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))
# Setup
setup(
    name='django-prefab',
    version=verstr,
    url='https://github.com/mc706/django-prefab',
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    license='MIT License',
    packages=['prefabricate'],
    include_package_data=True,
    description='Configuration driven Django Project Prefabricator',
    download_url = 'https://github.com/mc706/django-prefab/tarball/' + release,
    keywords = ['prefabricate', 'django', 'prefab'],
    entry_points={
        'console_scripts':[
            'prefabricate = prefabricate.main:main',
        ]
    },
    classifiers = [],
)