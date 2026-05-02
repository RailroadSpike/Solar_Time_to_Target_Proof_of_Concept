# proof of concept for calculating intercept time to a target in Solar cataphracts
# define a Hex class with q, r, s coordinates

# from fontTools.misc.cython import returns

# create functions for determining hex and euclidian distance between hexes
# create functions to calculate travel time based on distance to a hex
# Perhaps try some route optimization

# proof of concept does not include heat management or ship velocity vector.
# Assumes ship at rest traveling in a strait line

# import numpy as np  # may be needed for 3d arrays and some math
# import math
# import matplotlib.pyplot as plt  #  may be used in the future to draw our hexes and orbits
# from sympy import symbols  # may be used for some symbolic algebra later

from argparse import ArgumentParser

from gridHex import Hex
from gridHex import get_next_hex
from gridHex.utils import cubic_to_triax, triax_to_cubic
from ship import Ship
import test

if __name__ == '__main__':
    parser = ArgumentParser(prog="Solar Time to Target")
    parser.add_argument('-t', '--test', action='store_true', help='run tests and exit. Should be equivalent to running the following from the command line: `python -m unittest discover -v`')
    # parser.print_help()
    options = parser.parse_args()
    if options.test:
        print('\nTESTING...')
        test.run_all_tests()
