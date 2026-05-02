from .gridHex import Hex


# given two hex objects CURRENT and PREVIOUS, take their difference and then sum the difference with CURRENT
def getNextHex(currentHex, previousHex):
    diffX = currentHex.x - previousHex.x
    diffY = currentHex.y - previousHex.y
    diffZ = currentHex.z - previousHex.z

    sumX = currentHex.x + diffX  # sum difference with the current hex
    sumY = currentHex.y + diffY
    sumZ = currentHex.z + diffZ

    return Hex.initViaCubeCords(sumX, sumY, sumZ)  # initialize next hex and return it
