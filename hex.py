import math


# hex , defined using triaxials coordinates
# q axis is 60 degrees counter-clockwise of the vertical
# r axis vertical
# s axis is 60 degrees clockwise of the vertical
# HEX center to center distance D IS THE UNIT OF MEASUREMENT;  so all measurements can be considered to be a factor of D.
class Hex:
    def __init__(self, q,r,s):  # coordinates defining the hex; uses triax
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

    # returns the euclidian distances between the center of the two given hexes
    @classmethod
    def euclidDist(cls, hex1, hex2):
        return math.sqrt((hex1.xEuc - hex2.xEuc) ** 2 + (hex1.yEuc - hex2.yEuc) ** 2)  # pythagoras type shi

    # prints some basic info about the hex,
    # also in progress
    def __str__(self):  # prints the q,r,s of the hex in appropriate format
        return ' , '.join([str(x) for x in [self.q, self.r, self.s]])
