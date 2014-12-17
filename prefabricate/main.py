import os
import json
from argparse import ArgumentParser

from _setup_environment import setup_environment
from _setup_requirements import setup_requirements
from _setup_project import start_project


def main():
    """
    Main Loop for django fabrication
    """
    parser = ArgumentParser("Run a prefabrication configuration file")
    parser.add_argument('config_file', metavar="configfile", nargs=1, help="Configuration File for prefabrication")
    args = parser.parse_args()
    config_path = os.path.join(os.getcwd(), args.config_file[0])
    with open(config_path, 'r') as config_file:
        blueprint = json.loads(config_file.read())

    # setup environment
    setup_environment(blueprint)
    setup_requirements(blueprint)
    start_project(blueprint)



