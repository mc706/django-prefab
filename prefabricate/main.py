from argparse import ArgumentParser

def main():
    """
    Main Loop for django fabrication
    """
    parser = ArgumentParser("Run a prefabrication configuration file")
    parser.add_argument('config_file', metavar="configfile", nargs=1, help="Configuration File for prefabrication")
    args = parser.parse_args()
    print args.config_file
    with open(args.config_file, 'r') as f:
        contents = f.read()
    return "Confirguration:\n %s" % contents
