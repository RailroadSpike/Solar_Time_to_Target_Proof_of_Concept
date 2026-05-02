# class that models ship manouver behavior. Ships calculate their next hex

# From 0.5 ruleset:
# Ships are always either docked at a station, or moving through space at some velocity, including zero.
# When moving through space, each day, the ship travels hexes equal to its current velocity, moving it through the void
# towards a specific hex.
# With solar sails, within 100 hexes of the stars, any ship at v1 or greater can change its angle of flight by a single
# hex port or starboard, at no cost to the vessel.
# After that change, the ship can spend [SIZE] hydrogen to burn its engines to change its destination by one hex in any
# direction.
# If the new hex is further away, the ship's velocity is increased, if it’s nearer, the velocity is decreased, so
# velocity is always a count of how many hexes are travelled through.

# solar sails not implemented

import gridHex


class Ship:
    # ships are initialized with a location, assumed to start with 0 velocity (next hex same as current hex)
    def __init__(self, q_start, r_start, s_start):
        # ship "velocity" is defined by two hexes, its current hex its hex tomorrow (next hex)
        # the velocity vector is calculated based on the current and previous hexes.
        self.currentHex = gridHex.Hex(q_start, r_start, s_start)
        self.previousHex = gridHex.Hex(q_start, r_start, s_start)
        # The next hex is calculated by applying the velocity vector to the current hex, then applying any burn orders
        self.nextHex = gridHex.Hex(q_start, r_start, s_start)

        # self.currentDay = 0  # current day of the trip.  Trips start at day 0
        # ship's current burn order. 0 is a burn in the r axis direction, increments clockwise.  -1 is no burn order.
        self.currentBurnOrder = -1
        # self.currentHeat = 0  # heat information; not implemented yet.
        # self.maxHeat = 0
        # not really speed, this tracks how many "prograde" burns the ship has performed.
        # This info is needed for deceleration calculations
        # self.currentSpeed = 0
        # ditto, not speed but the number of prograde burns the ship is allowed to perform on the trip
        # self.maxSpeed = 0
        # hexes the ship has occupied, held in an array. appends every day, regardless of if the ship moved.
        # cleared when a trip starts for testing simplicity
        self.hexHistory = []
        # burn orders for the ship.  appends each day, no matter if the ship had a burn order.
        # Cleared when a trip starts for testing simplicity.
        self.burnHistory = []

        # ship state machine for a trip between two hexes.
        # Every time an ingame day ticks over, the ship determines its state for the next day. See tick day function
        # 0 : begin
        # 1 : burn
        # 2 : cruise + vent
        # 3 : decelerate
        # 4 : arrived
        # self.currentState =  0
        # self.nextState = 0
        # self.stateHistory =[]

    # sets current hex of the ship; used for initialization
    def set_current_hex(self, hex):
        self.currentHex = hex
        return

    # sets next hex of the ship.  for initialization and testing;
    def set_next_hex(self, hex):
        self.nextHex = hex
        return

    # sets burn order variable, and updates the next hex if necessary.
    # -1 is no burn order.  0 is a burn order in the q axis.  directions increment clockwise
    def set_burn_order(self, new_burn_order):

        if self.currentBurnOrder == new_burn_order:  # if the orders are the same, do nothing and return
            return

        else:
            # different cases for no burn order (-1) vs others
            if new_burn_order == -1:
                # if no burn order, the ship drifts the same distance as it did the previous iteration
                self.nextHex = gridHex.get_next_hex(self.currentHex, self.previousHex)
                return
            else:
                # if there is a burn order, the ship changes its next hex location by one in that direction
                # calculate the next hex from the current and previous hexes
                velocity_target_hex = gridHex.get_next_hex(self.currentHex, self.previousHex)
                # get the neighbor of the velocity target in the
                self.nextHex = velocity_target_hex.get_neighbor(self.currentBurnOrder)
            return

    # decelrate:  pick a hex that moves the ship towards the target but decreases the hexes traversed tomorrow
    # accelerate:  pick the hex that moves the ship closest to its target

    # Tick day:  When the day ticks over, move the ship and then calculate the next state.
    # This will eventually be used for the ship state machine.
    def tick_day(self):
        # create new current location hex and append it to the hex History array
        today_hex = gridHex.Hex(self.currentHex.q, self.currentHex.r, self.curretHex.s)
        # subtract the next hex from the current hex to get the distance vector
        # move the ship ( next hex becomes current hex)
        # append burn order to the history
        # clear burn order
        # calculate next hex
        return

    # Intended for debugging the ship class; not used for the ship state machine.
    # a more generalized function to move the ship to the next hex.
    def move_ship(self):
        self.hexHistory.append(self.currentHex)  # save location history information
        self.burnHistory.append(self.currentBurnOrder)  # save burn order history information
        self.currentBurnOrder = -1  # clear burn order
        self.previousHex = self.currentHex  # update previous hex to the current hex
        self.currentHex = self.nextHex  # update the current hex to the nextHex
        self.nextHex = gridHex.get_next_hex(self.currentHex, self.previousHex)  # calculate next hex, if ship drifts
        return
