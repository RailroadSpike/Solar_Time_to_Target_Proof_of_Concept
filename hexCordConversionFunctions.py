# conversion functions to convert between triaxial qrs and cubic xyz coordinates
from gridHex import Hex


# given a set of q,r,s triax coordianes,
# from Ske
def triaxToCubic(q,r,s) :
    x = 0
    y = -q - r - x
    z = q + x

    if (s < 0 and q > 0):  # or (y < 0 and z > 0):
        if r > 0:
            x = -q
            y = -r
            z = 0
        else:
            x = -q - r
            y = 0
            z = r
    elif (s > 0 and q < 0):  # or (y > 0 and z < 0):
        if r < 0:
            x = -q
            y = -r
            z = 0
        else:
            x = -q - r
            y = 0
            z = r
    return x, y, z

# given a set f x,y,z cubic coordinates, return triax coordinates
# from Ske
def cubicToTriax(x,y,z) :
    q = -x + z
    r = -y - z
    s = -q - r
    return q, r, s

# given a set of x,y,z cube cords, return a hex with the correct q r s coordinates.
# VERY FUCKED THAT THIS IS HERE; MAYBE THIS FUNCTIONALITY SHOULD BE PART OF THE HEX CLASS
def initialzeViaCubeCords(x,y,z):
    q,r,s = cubicToTriax(x,y,z) # conver the given cubic cords to triax
    return Hex(q,r,s)

# given two hex objects CURRENT and PREVIOUS, take their difference and then sum the difference with CURRENT
def getNextHex(currentHex, previousHex) :
    diffX = currentHex.x - previousHex.x
    diffY = currentHex.y - previousHex.y
    diffZ = currentHex.z - previousHex.z

    sumX = currentHex.x + diffX   # sum difference with the current hex
    sumY = currentHex.y + diffY
    sumZ = currentHex.z + diffZ

    return initialzeViaCubeCords(sumX,sumY, sumZ) # initialize next hex and return it