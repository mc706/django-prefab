from argparse import ArgumentParser
import os


def main():
    """
    Main Loop for django fabrication
    """
    parser = ArgumentParser("Run a prefabrication configuration file")
    parser.add_argument('config_file', metavar="configfile", nargs=1, help="Configuration File for prefabrication")
    args = parser.parse_args()
    blueprint = os.path.join(os.getcwd(), args.config_file[0])
    print blueprint
    with open(blueprint, 'r') as f:
        contents = f.read()
    return "Confirguration:\n %s" % contents
