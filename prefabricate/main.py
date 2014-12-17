from argparse import ArgumentParser

def main():
    """
    Main Loop for django fabrication
    """
    parser = ArgumentParser("Run a prefabrication configuration file")
    parser.add_argument('config_file', metavar="configfile", nargs=1, help="Configuration File for prefabrication")
    config_file = parser.parse_args()
    with open(config_file, 'r') as f:
        contents = f.read()
    return "Confirguration:\n %s" % contents
