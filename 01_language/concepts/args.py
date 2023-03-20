# this is an example of mutually exclusive group.

import argparse

def get_args():
    """
    A function as an example to argument parsing
    """
    parser = argparse.ArgumentParser(
        description="A simple arg parser",
        epilog="This is where you might example usage"
    )
    
    group = parser._mutually_exclusive_groups()
    group.add_argument("-x", "--execute", action="store", help="Help text for x")
    group.add_argument("-y", default=False, help="Help text for y")
    parser.add_argument("-z", type=int, help="Help text for z")

    print(parser.parse_args())

if __name__ == "__main__":
    get_args()
    

# ➜ python-a2z (main) ✗ python 01_language/concepts/args.py -x abc -y def
# Traceback (most recent call last):
#   File "/Users/niteshchauhan/Desktop/code/learn/python/python-a2z/01_language/concepts/args.py", line 20, in <module>
#     get_args()
#   File "/Users/niteshchauhan/Desktop/code/learn/python/python-a2z/01_language/concepts/args.py", line 12, in get_args
#     group = parser._mutually_exclusive_groups()
# TypeError: 'list' object is not callable