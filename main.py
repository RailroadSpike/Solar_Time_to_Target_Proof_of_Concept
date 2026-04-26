# proof of concept for calculating intercept time to a target in Solar cataphracts
# define a Hex class with q,r,s coordinates


from fontTools.misc.cython import returns

# create functions for determining hex and euclidian distance between hexes
# create functions to calculate travel time based on distance to a hex
# Perhaps try some route optimization

# proof of concept does not include heat management or ship velocity vector.  Assumes ship at rest traveling in a strait line

# import numpy as np  #may be needed for 3d arrays and some math
# import math
# import matplotlib.pyplot as plt  #  may be used in the future to draw our hexes and orbits
# from sympy import symbols # may be used for some symbolic algebra later

import unittest
from gridHex import Hex

class TestHex(unittest.TestCase):
    # one hex per quadrant
    #testHex1 = Hex(3, 4, 0)
    #testHex2 = Hex(0, 2, 4)
    #testHex3 = Hex(-4, 0, 1)
    #testHex4 = Hex(-2, -1, 0)
    #testHex5 = Hex(0, -1, -3)
    #testHex6 = Hex(2, 0, -2)
    #testHex7 = Hex(0, 0, 3)

    def test_getNeighbor(self):
        testHex1 = Hex(3, 4, 0)
        testHex3 = Hex(-4, 0, 1)
        testHex7 = Hex(0, 0, 3)

        self.assertTrue(testHex1.getNeighbor(0), (3,5,0))
        self.assertTrue(testHex1.getNeighbor(1), (2,6,0))
        self.assertTrue(testHex1.getNeighbor(2), (2,5,0))
        self.assertTrue(testHex1.getNeighbor(3), (3,3,0))
        self.assertTrue(testHex1.getNeighbor(4), (4,4,0))
        self.assertTrue(testHex1.getNeighbor(5), (4,5,0))
        print("first set done")
        self.assertTrue(testHex3.getNeighbor(0), (-3,0,2))
        self.assertTrue(testHex3.getNeighbor(1), (-4,0,2))
        self.assertTrue(testHex3.getNeighbor(2), (-5,0,1))
        self.assertTrue(testHex3.getNeighbor(3), (-5,0,0))
        self.assertTrue(testHex3.getNeighbor(4), (-4,0,0))
        self.assertTrue(testHex3.getNeighbor(5), (-3,0,1))
        print("Second set done")
        self.assertTrue(testHex7.getNeighbor(0), (0, 1, 3))
        self.assertTrue(testHex7.getNeighbor(1), (0, 0, 4))
        self.assertTrue(testHex7.getNeighbor(2), (-1, 0, 3))
        self.assertTrue(testHex7.getNeighbor(3), (-1, 0, 2))
        self.assertTrue(testHex7.getNeighbor(4), (0, 0, 0))
        self.assertTrue(testHex7.getNeighbor(5), (0, 1, 2))
        print("third set done")

if __name__ == '__main__':
    unittest.main()
