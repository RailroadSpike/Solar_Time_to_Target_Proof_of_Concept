import math


# hex , defined using triaxials coordinates
# HEX center to center distance D IS THE UNIT OF MEASUREMENT;  so all measurements can be considered to be a factor of D.
class Hex:
    def __init__(self, q, r, s):  # coordinates defining the hex; uses triax
        assert q==0 or r==0 or s==0  # triaxial shortest path constraint
        self.q = q  # q axis is 60 degrees counter-clockwise of the vertical
        self.r = r  # r axis vertical
        self.s = s  # s axis is 60 degrees clockwise of the vertical

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

        # append vert 1 coordinates
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
        q = self.q
        r = self.r
        s = self.s
        if direction == 0:
            r += 1
        elif direction == 1:
            s += 1
        elif direction == 2:
            q -= 1
        elif direction == 3:
            r -= 1
        elif direction == 4:
            s -= 1
        elif direction == 5:
            q += 1
        return q, r, s

    # hex mathematics functions

    # returns the euclidian distances between the center of the two given hexes
    @classmethod
    def euclidDist(cls, hex1, hex2):
        return math.sqrt((hex1.xEuc - hex2.xEuc) ** 2 + (hex1.yEuc - hex2.yEuc) ** 2)  # pythagoras type shi

    # returns the manhattan hex distance between hex1 and hex2.  Im SURE there is a more eligant
    # solution, but this is what I could figure out after staring at the problem for DAYS
    @classmethod
    def hexDist(cls, hex1, hex2):
        # convert to two axis q, r format, called dubAxis format in this function. hold the 2 axis hexes in arrays for simplicity, [q,r]
        dubAxis1 = []
        dubAxis2 = []
        dubAxisDiff = []
        dubAxis1.append(hex1.q - hex1.s)  # moving +1 in the s axis is equivalent to moving -1 q and +1 r,
        dubAxis1.append(hex1.r + hex1.s)

        dubAxis2.append(hex2.q - hex2.s)  # convert both qrs hexes
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

    # prints some basic info about the hex,
    # also in progress
    def __str__(self):  # prints the q,r,s of the hex in appropriate format
        return ' , '.join([str(x) for x in [self.q, self.r, self.s]])
