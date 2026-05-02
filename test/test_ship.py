import unittest

from ship import Ship


class TestShip(unittest.TestCase):

    def test_init(self):
        test_ship = Ship(0, 2, 0)
        # check that the current, previous, next hexes are initialized.
        # self
        self.assertTrue(test_ship.currentHex.q == 0)
        self.assertTrue(test_ship.currentHex.r == 2)
        self.assertTrue(test_ship.currentHex.s == 0)

        self.assertTrue(test_ship.previousHex.q == 0)
        self.assertTrue(test_ship.previousHex.r == 2)
        self.assertTrue(test_ship.previousHex.s == 0)

        self.assertTrue(test_ship.nextHex.q == 0)
        self.assertTrue(test_ship.nextHex.r == 2)
        self.assertTrue(test_ship.nextHex.s == 0)

        # check that the current burn order is -1 (no burn order)
        self.assertTrue(test_ship.currentBurnOrder == -1)
