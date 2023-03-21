# cooking.py

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--coordinates", nargs=2)
parser.add_argument("veggies", nargs="+")
parser.add_argument("fruits", nargs="*")
parser.add_argument("--size", choices=["S", "M", "L", "XL"], default="M")
parser.add_argument("--weekday", type=int, choices=range(1, 8))

args = parser.parse_args()

print(args)

# $ python cooking.py --veggies pepper tomato --fruits apple banana
# Namespace(veggies=['pepper', 'tomato'], fruits=['apple', 'banana'])