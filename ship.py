# class that models ship manouver behavior. Ships calculate their next hex

# From 0.5 ruleset:
# Ships are always either docked at a station, or moving through space at some velocity, including zero.
# When moving through space, each day, the ship travels hexes equal to its current velocity, moving it through the void towards a specific hex.
# With solar sails, within 100 hexes of the stars, any ship at v1 or greater can change its angle of flight by a single hex port or starboard, at no cost to the vessel.
# After that change, the ship can spend [SIZE] hydrogen to burn its engines to change its destination by one hex in any direction.
# If the new hex is further away, the ship's velocity is increased, if it’s nearer, the velocity is decreased, so velocity is always a count of how many hexes are travelled through.

# solar sails not implemented

from gridHex import Hex
from hexCordConversionFunctions import getNextHex


class ship:
    def __init__(self, qStart, rStart, sStart):  # ships are initialized with a location, assumed to start with 0 velocity (next hex same as current hex)
        self.currentHex = Hex(qStart,rStart, sStart) # ship "velocity" is defined by two hexes, its current hex its hex tomorrow (next hex)
        self.previousHex = Hex(qStart,rStart, sStart)  # the velocity vector is calculated based on the current and previous hexes.
        self.nextHex = Hex(qStart,rStart, sStart) # The next hex is calculated by applying the velocity vector to the current hex, then applying any burn orders

        #self.currentDay = 0  # current day of the trip.  Trips start at day 0
        self.currentBurnOrder = -1      # ship's current burn order. 0 is a burn in the r axis direction, increments clockwise.  -1 is no burn order.
        #self.currentHeat = 0  # heat information; not implemented yet.
        #self.maxHeat = 0
        #self.currentSpeed = 0  # not really speed, this tracks how many "prograde" burns the ship has performed.  This info is needed for deceleration calculations
        #self.maxSpeed = 0       # ditto, not speed but the number of prograde burns the ship is allowed to perform on the trip
        self.hexHistory = []  # hexes the ship has occupied, held in an array. appends every day, regardless of if the ship moved.  cleared when a trip starts for testing simplicity
        self.burnHistory = [] # burn orders for the ship.  appends each day, no matter if the ship had a burn order.  Cleared when a trip starts for testing simplicity.

        # ship state machine for a trip between two hexes.  Every time an ingame day ticks over, the ship determines its state for the next day. See tick day function
        # 0 : begin
        # 1 : burn
        # 2 : cruise + vent
        # 3 : decelerate
        # 4 : arrived
        #self.currentState =  0
        #self.nextState = 0
        #self.stateHistory =[]

        # sets current hex of the ship; used for initialization
        def setCurrentHex(self, Hex):
            self.currentHex = Hex
            return

        # sets next hex of the ship.  for initialization and testing;
        def setNextHex(self, Hex):
            self.nextHex = Hex
            return

        # sets burn order variable, and updates the next hex if necessary.
        # -1 is no burn order.  0 is a burn order in the q axis.  directions increment clockwise
        def setBurnOrder(self, newBurnOrder):

            if self.currentBurnOrder == newBurnOrder: # if the orders are the same, do nothing and return
                return

            else :
                # different cases for no burn order (-1) vs others
                if newBurnOrder == -1 :
                    self.nextHex = getNextHex(self.currentHex, self.previousHex) # if no burn order, the ship drifts the same distance as it did the previous iteration
                    return
                else:
                    # if there is a burn order, the ship changes its next hex location by one in that direction
                    velocityTargetHex = getNextHex(self.currentHex, self.previousHex) # calculate the next hex from the current and previous hexes
                    self.nextHex = velocityTargetHex.getNeighbor(self.currentBurnOrder) # get the neighbor of the velocity target in the
                return
            
        # decelrate:  pick a hex that moves the ship towards the target but decreases the hexes traversed tomorrow
        # accelerate:  pick the hex that moves the ship closest to its target

        # Tick day:  When the day ticks over, move the ship and then calculate the next state.  This will eventually be used for the ship state machine.
        def tickDay(self):
            todayHex = Hex(self.currentHex.q, self.currentHex.r, self.curretHex.s)  # create new current location hex and append it to the hex History array
            # subtract the next hex from the current hex to get the distance vector
            # move the ship ( next hex becomes current hex)
            # append burn order to the history
            # clear burn order
            # calculate next hex
            return

        # Intended for debugging the ship class; not used for the ship state machine.
        # a more generalized function to move the ship to the next hex.
        def moveShip(self):
            self.hexHistory.append(self.currentHex)  # save location history information
            self.burnHistory.append(self.currentBurnOrder)  # save burn order history information
            self.currentBurnOrder = -1 # clear burn order
            self.previousHex = self.currentHex # update previous hex to the current hex
            self.currentHex = self.nextHex # update the current hex to the nextHex
            self.nextHex = getNextHex(self.currentHex,self.previousHex) # calculate the next hex, if the ship drifts
            return


