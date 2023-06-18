# The .exit() method is appropriate when you need complete control over which status code to return. On the other hand, the .error() method is internally used by argparse for command-line syntax errors

import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument("--coordinates", nargs=2)
args = parser.parse_args()

if len(sys.argv) != 4:
    parser.error("wrong number of args")

if not isinstance(args.coordinates, list):
    parser.exit(1, message="The coordinates are not in a list")

print(args)

