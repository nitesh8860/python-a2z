import argparse

def get_args():
    """
    A function as an example to argument parsing
    """
    parser = argparse.ArgumentParser(
        description="A simple arg parser",
        epilog="This is where you might example usage"
    )
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-x", "--execute", action="store", help="Help text for x")
    group.add_argument("-y", default=False, help="Help text for y")
    parser.add_argument("-z", type=int, help="Help text for z") 

    args = parser.parse_args()
    print(args)
    print(args.execute)

if __name__ == "__main__":
    get_args()
    
# this is an example of mutually exclusive group.

# ➜ python-a2z (main) ✗ python 01_language/concepts/args.py -x abc -y def
# usage: args.py [-h] [-x EXECUTE | -y Y] [-z Z]
# args.py: error: argument -y: not allowed with argument -x/--execute