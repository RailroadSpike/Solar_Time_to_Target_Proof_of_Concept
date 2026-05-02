from gridHex import Hex


# planet class i havent really implemented yet
class CelestialBody:
    def __init__(self, inputRadius, inputDir, startingQ, startingR, startingS):
        # for this example, all orbits are assumed to be circular.
        # the starting hex is assumed to be on the circular orbit.  The
        self.orbitRadius = inputRadius
        self.startingHex = Hex(startingQ, startingR, startingS)  # initialize the starting hex object
        self.center = Hex(0, 0, 0)                        # middle of the grid; we will need this for radius calc.
        self.orbitDir = inputDir    # 0 for clockwise orbit, 1 for counterclockwise orbit.
        # array of hex objects which form the orbit;
        # the index of this array is the location of the celestial body at day index
        self.orbitHexList = []

        # time to determine which hexes comprise the celestial body's orbit.
