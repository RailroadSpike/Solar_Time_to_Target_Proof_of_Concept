# proof of concept for calculating intercept time to a target in Solar cataphracts
# define a Hex class with q,r,s coordinates

# create functions for determining hex and euclidian distance between hexes
# create functions to calculate travel time based on distance to a hex
# Perhaps try some route optimization

# proof of concept does not include heat management or ship velocity vector.  Assumes ship at rest traveling in a strait line

#import numpy as np  #may be needed for 3d arrays and some math
import math
#import matplotlib.pyplot as plt  #  may be used in the future to draw our hexes and orbits
#from sympy import symbols # may be used for some symbolic algebra later

from hex import Hex


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


if __name__ == '__main__':
    hex1 = Hex(2, 4, 0)
    hex2 = Hex(-3, 0, 2)

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

