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
from gridHex import Hex, triaxToCubic, cubicToTriax, initViaCubeCords, getNextHex
from ship import ship



class TestHex(unittest.TestCase):
    # one hex per quadrant, plus a hex on an axis
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
        #print("first set done")
        self.assertTrue(testHex3.getNeighbor(0), (-3,0,2))
        self.assertTrue(testHex3.getNeighbor(1), (-4,0,2))
        self.assertTrue(testHex3.getNeighbor(2), (-5,0,1))
        self.assertTrue(testHex3.getNeighbor(3), (-5,0,0))
        self.assertTrue(testHex3.getNeighbor(4), (-4,0,0))
        self.assertTrue(testHex3.getNeighbor(5), (-3,0,1))
        #print("Second set done")
        self.assertTrue(testHex7.getNeighbor(0), (0, 1, 3))
        self.assertTrue(testHex7.getNeighbor(1), (0, 0, 4))
        self.assertTrue(testHex7.getNeighbor(2), (-1, 0, 3))
        self.assertTrue(testHex7.getNeighbor(3), (-1, 0, 2))
        self.assertTrue(testHex7.getNeighbor(4), (0, 0, 0))
        self.assertTrue(testHex7.getNeighbor(5), (0, 1, 2))
        #print("third set done")

    def test_triaxToCubic(self):
        testHex1 = Hex(3, 1, 0)
        testHex3 = Hex(-2, -2, 0)
        testHex7 = Hex(0, 0, 3)

        #print(testHex1.x,testHex1.y,testHex1.z)
        #print(triaxToCubic(3,1,0))
        self.assertTrue(testHex1.x,-3)
        self.assertTrue(testHex1.y,-1)
        self.assertTrue(testHex1.z,4)

        #print(triaxToCubic(-2,-2,0))
        self.assertTrue(testHex3.x,2)
        self.assertTrue(testHex3.y,2)
        self.assertTrue(testHex3.z,-4)

        #print(triaxToCubic(0, 0, 3))
        self.assertTrue(testHex7.x,3)
        self.assertTrue(testHex7.y,-3)
        self.assertTrue(testHex7.z==0)

    def test_cubicToTriax(self):
        testHex1 = Hex(3, 1, 0)
        testHex3 = Hex(-2, -2, 0)
        testHex7 = Hex(0, 0, 3)

        q,r,s = cubicToTriax(testHex1.x, testHex1.y, testHex1.z)
        #print(q,r,s)
        self.assertTrue(q, 3)
        self.assertTrue(r, 1)
        self.assertTrue(s==0)

        q,r,s = cubicToTriax(testHex3.x, testHex3.y, testHex3.z)
        #print(q,r,s)
        self.assertTrue(q, -2)
        self.assertTrue(r, -2)
        self.assertTrue(s==0)

        q,r,s = cubicToTriax(testHex7.x, testHex7.y, testHex7.z)
        #print(q,r,s)
        self.assertTrue(q==0)
        self.assertTrue(r==0)
        self.assertTrue(s==3)

    def test_initViaCubeCords(self):
        #testHex1 = Hex(3, 1, 0)
        #testHex2 = Hex(-2, -2, 0)
        #testHex3 = Hex(0, 0, 3)

        x1 = -3
        y1 = -1
        z1 = 4

        x2 = 2
        y2 = 2
        z2 = -4

        x3 = 3
        y3 = -3
        z3 = 0

        hex1 = initViaCubeCords(x1,y1,z1)
        hex2 = initViaCubeCords(x2,y2,z2)
        hex3 = initViaCubeCords(x3,y3,z3)

        #print(hex1)
        self.assertTrue(hex1.q==3)
        self.assertTrue(hex1.r==1)
        self.assertTrue(hex1.s==0)

        #print(hex2)
        self.assertTrue(hex2.q==-2)
        self.assertTrue(hex2.r==-2)
        self.assertTrue(hex2.s==0)

        #print(hex3)
        self.assertTrue(hex3.q==0)
        self.assertTrue(hex3.r==0)
        self.assertTrue(hex3.s==3)

    def test_getNextHex(self):
        testHex1 = Hex(0, 0, 0) #prev
        testHex2 = Hex(0, 2, 0) #current
        #next hex should be (0,0,4)

        testHex3 = Hex(-3, 0, 1) #prev
        testHex4 = Hex(-1, 0, 3) #current
        #next hex Should be (0,1,4)

        testHex5 = Hex(0, -1, -3) #prev
        testHex6 = Hex(1, 0, -1) #current
        # next hex should be (1,2,0)

        nextHex10 = getNextHex(testHex2,testHex1)
        nextHex20 = getNextHex(testHex4,testHex3)
        nextHex30 = getNextHex(testHex6,testHex5)

        #print(nextHex10)
        self.assertTrue(nextHex10.q==0)
        self.assertTrue(nextHex10.r==4)
        self.assertTrue(nextHex10.s==0)

        #print(nextHex20)
        self.assertTrue(nextHex20.q==0)
        self.assertTrue(nextHex20.r==1)
        self.assertTrue(nextHex20.s==4)

        #print(nextHex30)
        self.assertTrue(nextHex30.q == 1)
        self.assertTrue(nextHex30.r == 2)
        self.assertTrue(nextHex30.s == 0)

        # test more edge cases and longer trips
        testHex7 = Hex(-3, 0, 0)  # prev
        testHex8 = Hex(-1, 0, 0)  # current
        # next hex should be (1,0,0)

        testHex9 = Hex(3, 8, 0)  # prev
        testHex10 = Hex(0, 4, 1)  # current
        # next hex Should be (-3,0,2)

        testHex11 = Hex(2, 0, -2)  # prev
        testHex12 = Hex(0, 6, 0)  # current
        # next hex should be (0,10,4)

        nextHex40 = getNextHex(testHex8, testHex7)
        nextHex50 = getNextHex(testHex10, testHex9)
        nextHex60 = getNextHex(testHex12, testHex11)

        #print(nextHex40)
        self.assertTrue(nextHex40.q == 1)
        self.assertTrue(nextHex40.r == 0)
        self.assertTrue(nextHex40.s == 0)

        #print(nextHex50)
        self.assertTrue(nextHex50.q == -3)
        self.assertTrue(nextHex50.r == 0)
        self.assertTrue(nextHex50.s == 2)

        #print(nextHex60)
        self.assertTrue(nextHex60.q == 0)
        self.assertTrue(nextHex60.r == 10)
        self.assertTrue(nextHex60.s == 4)

    # `class test_ship

class TestShip(unittest.TestCase):

    def test_init(self):
        testShip = ship(0,2,0)
        #check that the current, previous, next hexes are initialized.
        self
        self.assertTrue(testShip.currentHex.q==0)
        self.assertTrue(testShip.currentHex.r==2)
        self.assertTrue(testShip.currentHex.s==0)

        self.assertTrue(testShip.previousHex.q==0)
        self.assertTrue(testShip.previousHex.r==2)
        self.assertTrue(testShip.previousHex.s==0)

        self.assertTrue(testShip.nextHex.q==0)
        self.assertTrue(testShip.nextHex.r==2)
        self.assertTrue(testShip.nextHex.s==0)

        self.assertTrue(testShip.currentBurnOrder==-1)

        #check that the current burn order is -1 (no burn order)
        return

if __name__ == '__main__':
    unittest.main()
