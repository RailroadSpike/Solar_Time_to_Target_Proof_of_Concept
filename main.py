# proof of concept for determining a circular orbit
# define a Hex class with q,r,s coordinates
# define a Universe class, consisting of 3d matrix Hex objects, stored in a three-dimensional matrix
#   The univers also defines a universal radius, which is the distance between the center of two hexes
#   The center of the univers is coordinate 0,0,0

# Define CelestialBody class
#   CelstialBody has an orbit radius as a factor of the universal radius
#   CelstialBody has a starting hex, which is orbit_radius from the center of the univers.  This is defined as a
#   CelestialBody has an orbit, which is an ordered list starting at the starting hex, and includes every hex which is part of its orbit

import numpy as np  #need this for 3d arrays and some math
import math
import matplotlib.pyplot as plt  # used to draw our hexes and orbits
from sympy import symbols #used to algebraically solve where


# hex grid, defined using triaxials coordinates
# q axis is 60 degrees counter-clockwise of the vertical
# r axis vertical
# s axis is 60 degrees clockwise of the vertical
# HEX HEIGHT D IS THE UNIT OF MEASUREMENT;  so all measurements can be considered to be a factor of D.
class Hex:
    def __init__(self, q,r,s):  # coordinates defining the hex; uses cubic coordinates
        self.q = q
        self.r = r
        self.s = s

        self.vertsXArray = []
        self.vertsYArray = []

        # Calculate and store the euclidian coordinates of the center of the hex.  x/y coordinates stored in an array self.center
        self.xEuc = - math.sqrt(3)*0.5*self.q + math.sqrt(3)*0.5*self.s  # derived using vector addition.
        self.yEuc = 0.5*self.q + r + 0.5*self.s  # derived using vector addition.
        self.center = []  # euclidian coords stored as x,y, stored an as array for easier access
        self.center.append(self.xEuc)
        self.center.append(self.yEuc)

        # Verticie locations of the hex; vert 0 is first clockwise from r axis, increases clockwise.
        # vert locations are calculated relative to the center of the hex. just a bit of trig
        # these will be important for drawing hexes later.

        # append vert 0 coordinates
        self.vertsXArray.append(self.xEuc + 1 / (2 * math.sqrt(3)))
        self.vertsYArray.append(self.yEuc + 0.5)

        #append vert 1 coordinates
        self.vertsXArray.append(self.xEuc + 0.5)
        self.vertsYArray.append(self.yEuc)

        # append vert 2 cords
        self.vertsXArray.append(self.xEuc + 1 / (2 * math.sqrt(3)))
        self.vertsYArray.append(self.yEuc - 0.5)

        # append vert 3 cords
        self.vertsXArray.append(self.xEuc - 1 / (2 * math.sqrt(3)))
        self.vertsYArray.append(self.yEuc - 0.5)

        # append vert 4 cords
        self.vertsXArray.append(self.xEuc - 0.5)
        self.vertsYArray.append(self.yEuc)

        # append vert 5 cords
        self.vertsXArray.append(self.xEuc - 1 / (2 * math.sqrt(3)))
        self.vertsYArray.append(self.yEuc + 0.5)

        # get the q,r,s coordinates in the next hex in a given direction.  0 is along the r axis, directions increment clockwise
        # in progress
    def getNeighbor(self, direction):
        # if direction == 0:
        return

    def printHex(self): #prints the q,r,s of the hex in appropriate format
        print(self.q, ',', self.r, ',', self.s)
        return




# hex mathematics functions

# returns the manhattan hex distance between hex1 and hex2.  Im SURE there is a more eligant
# solution, but this is what I could figure out after staring at the problem for DAYS
def hexDist(hex1, hex2):
    #convert to two axis q, r format, called dubAxis format in this function. hold the 2 axis hexes in arrays for simplicity, [q,r]
    dubAxis1 = []
    dubAxis2 = []
    dubAxisDiff = []
    dubAxis1.append(hex1.q - hex1.s)            # moving +1 in the s axis is equivalent to moving -1 q and +1 r,
    dubAxis1.append(hex1.r + hex1.s)

    dubAxis2.append(hex2.q - hex2.s)            # convert both qrs hexes
    dubAxis2.append(hex2.r + hex2.s)

    # take the difference of the two hex coordinates
    dubAxisDiff.append(dubAxis1[0] - dubAxis2[0])
    dubAxisDiff.append(dubAxis1[1] - dubAxis2[1])

    # logic for the distahce:
    # if the difference vector q and r components have the same sign, the distance is the absolute value of their sum
    # if the difference vector q and r components have different signs, OR if one component is zero, the distances is the absolute max of the two
    #   THIS WAS DERIVED OBSERVATIONALLY DO NOT ASK ME WHY
    if dubAxisDiff[0] * dubAxisDiff[1] > 0:  # check if the two components of the difference have the same sign
        return abs(dubAxisDiff[0]) + abs(dubAxisDiff[1])
    else:
        return max(abs(dubAxisDiff[0]), abs(dubAxisDiff[1]))


# returns the euclidian distances between the center of the two given hexes
def euclidDist(hex1, hex2):

    return math.sqrt((hex1.xEuc - hex2.xEuc)**2 + (hex1.yEuc - hex2.yEuc)**2) # pythagoras type shi


class CelestialBody:
    def __init__(self, inputRadius, inputDir, startingQ, startingR, startingS):
        self.orbitRadius = inputRadius # for this example, all orbits are assumed to be circular.  the starting hex is assumed to be on the circular orbit.  The
        self.startingHex = Hex(startingQ, startingR, startingS)  # initialize the starting hex object
        self.center = Hex(0,0,0)                        # middle of the grid; we will need this for radius calc.
        self.orbitDir = inputDir    # 0 for clockwise orbit, 1 for counterclockwise orbit.
        self.orbitHexList = [] # array of hex objects which form the orbit; the index of this array is the location of the celestial body at day index

        # time to determine which hexes comprise the celestial body's orbit.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hex1 = Hex(2,4,0)
    hex2 = Hex(-3,0,2)

    hex1.printHex()
    print("\n")
    hex2.printHex()
    print("\n")

    print(hex1.xEuc, ',', hex1.yEuc)
    print("\n")
    print(hex2.xEuc, ',', hex2.yEuc)
    print("\n")

    print("hex distance between hexes is: ")
    print(hexDist(hex1, hex2))
    print("\n")
    print("Euclidian distance between hexes is: ")
    eDistance = euclidDist(hex1, hex2)
    print(eDistance)
    print('end')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
