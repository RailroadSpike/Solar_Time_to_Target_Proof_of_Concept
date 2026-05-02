import unittest

from gridHex import Hex, get_next_hex
from gridHex.utils import cubic_to_triax


class TestHex(unittest.TestCase):
    # one hex per quadrant, plus a hex on an axis
    # testHex1 = Hex(3, 4, 0)
    # testHex2 = Hex(0, 2, 4)
    # testHex3 = Hex(-4, 0, 1)
    # testHex4 = Hex(-2, -1, 0)
    # testHex5 = Hex(0, -1, -3)
    # testHex6 = Hex(2, 0, -2)
    # testHex7 = Hex(0, 0, 3)

    def test_get_neighbor(self):
        test_hex1 = Hex(3, 4, 0)
        test_hex3 = Hex(-4, 0, 1)
        test_hex7 = Hex(0, 0, 3)

        self.assertTrue(test_hex1.get_neighbor(0), (3, 5, 0))
        self.assertTrue(test_hex1.get_neighbor(1), (2, 6, 0))
        self.assertTrue(test_hex1.get_neighbor(2), (2, 5, 0))
        self.assertTrue(test_hex1.get_neighbor(3), (3, 3, 0))
        self.assertTrue(test_hex1.get_neighbor(4), (4, 4, 0))
        self.assertTrue(test_hex1.get_neighbor(5), (4, 5, 0))
        # print("first set done")
        self.assertTrue(test_hex3.get_neighbor(0), (-3, 0, 2))
        self.assertTrue(test_hex3.get_neighbor(1), (-4, 0, 2))
        self.assertTrue(test_hex3.get_neighbor(2), (-5, 0, 1))
        self.assertTrue(test_hex3.get_neighbor(3), (-5, 0, 0))
        self.assertTrue(test_hex3.get_neighbor(4), (-4, 0, 0))
        self.assertTrue(test_hex3.get_neighbor(5), (-3, 0, 1))
        # print("Second set done")
        self.assertTrue(test_hex7.get_neighbor(0), (0, 1, 3))
        self.assertTrue(test_hex7.get_neighbor(1), (0, 0, 4))
        self.assertTrue(test_hex7.get_neighbor(2), (-1, 0, 3))
        self.assertTrue(test_hex7.get_neighbor(3), (-1, 0, 2))
        self.assertTrue(test_hex7.get_neighbor(4), (0, 0, 0))
        self.assertTrue(test_hex7.get_neighbor(5), (0, 1, 2))
        # print("third set done")

    def test_triax_to_cubic(self):
        test_hex1 = Hex(3, 1, 0)
        test_hex3 = Hex(-2, -2, 0)
        test_hex7 = Hex(0, 0, 3)

        # print(test_hex1.x, test_hex1.y, test_hex1.z)
        # print(triax_to_cubic(3, 1, 0))
        self.assertTrue(test_hex1.x, -3)
        self.assertTrue(test_hex1.y, -1)
        self.assertTrue(test_hex1.z, 4)

        # print(triax_to_cubic(-2, -2, 0))
        self.assertTrue(test_hex3.x, 2)
        self.assertTrue(test_hex3.y, 2)
        self.assertTrue(test_hex3.z, -4)

        # print(triax_to_cubic(0, 0, 3))
        self.assertTrue(test_hex7.x, 3)
        self.assertTrue(test_hex7.y, -3)
        self.assertTrue(test_hex7.z == 0)

    def test_cubic_to_triax(self):
        test_hex1 = Hex(3, 1, 0)
        test_hex3 = Hex(-2, -2, 0)
        test_hex7 = Hex(0, 0, 3)

        q, r, s = cubic_to_triax(test_hex1.x, test_hex1.y, test_hex1.z)
        # print(q, r, s)
        self.assertTrue(q, 3)
        self.assertTrue(r, 1)
        self.assertTrue(s == 0)

        q, r, s = cubic_to_triax(test_hex3.x, test_hex3.y, test_hex3.z)
        # print(q, r, s)
        self.assertTrue(q, -2)
        self.assertTrue(r, -2)
        self.assertTrue(s == 0)

        q, r, s = cubic_to_triax(test_hex7.x, test_hex7.y, test_hex7.z)
        # print(q, r, s)
        self.assertTrue(q == 0)
        self.assertTrue(r == 0)
        self.assertTrue(s == 3)

    def test_init_via_cube_cords(self):
        # testHex1 = Hex(3, 1, 0)
        # testHex2 = Hex(-2, -2, 0)
        # testHex3 = Hex(0, 0, 3)

        x1 = -3
        y1 = -1
        z1 = 4

        x2 = 2
        y2 = 2
        z2 = -4

        x3 = 3
        y3 = -3
        z3 = 0

        hex1 = Hex.init_via_cube_cords(x1, y1, z1)
        hex2 = Hex.init_via_cube_cords(x2, y2, z2)
        hex3 = Hex.init_via_cube_cords(x3, y3, z3)

        # print(hex1)
        self.assertTrue(hex1.q == 3)
        self.assertTrue(hex1.r == 1)
        self.assertTrue(hex1.s == 0)

        # print(hex2)
        self.assertTrue(hex2.q == -2)
        self.assertTrue(hex2.r == -2)
        self.assertTrue(hex2.s == 0)

        # print(hex3)
        self.assertTrue(hex3.q == 0)
        self.assertTrue(hex3.r == 0)
        self.assertTrue(hex3.s == 3)

    def test_get_next_hex(self):
        test_hex1 = Hex(0, 0, 0)  # prev
        test_hex2 = Hex(0, 2, 0)  # current
        # next hex should be (0, 0, 4)

        test_hex3 = Hex(-3, 0, 1)  # prev
        test_hex4 = Hex(-1, 0, 3)  # current
        # next hex Should be (0, 1, 4)

        test_hex5 = Hex(0, -1, -3)  # prev
        test_hex6 = Hex(1, 0, -1)  # current
        # next hex should be (1, 2, 0)

        next_hex10 = get_next_hex(test_hex2, test_hex1)
        next_hex20 = get_next_hex(test_hex4, test_hex3)
        next_hex30 = get_next_hex(test_hex6, test_hex5)

        # print(next_hex10)
        self.assertTrue(next_hex10.q == 0)
        self.assertTrue(next_hex10.r == 4)
        self.assertTrue(next_hex10.s == 0)

        # print(next_hex20)
        self.assertTrue(next_hex20.q == 0)
        self.assertTrue(next_hex20.r == 1)
        self.assertTrue(next_hex20.s == 4)

        # print(next_hex30)
        self.assertTrue(next_hex30.q == 1)
        self.assertTrue(next_hex30.r == 2)
        self.assertTrue(next_hex30.s == 0)

        # test more edge cases and longer trips
        test_hex7 = Hex(-3, 0, 0)  # prev
        test_hex8 = Hex(-1, 0, 0)  # current
        # next hex should be (1, 0, 0)

        test_hex9 = Hex(3, 8, 0)  # prev
        test_hex10 = Hex(0, 4, 1)  # current
        # next hex Should be (-3, 0, 2)

        test_hex11 = Hex(2, 0, -2)  # prev
        test_hex12 = Hex(0, 6, 0)  # current
        # next hex should be (0, 10, 4)

        next_hex40 = get_next_hex(test_hex8, test_hex7)
        next_hex50 = get_next_hex(test_hex10, test_hex9)
        next_hex60 = get_next_hex(test_hex12, test_hex11)

        # print(next_hex40)
        self.assertTrue(next_hex40.q == 1)
        self.assertTrue(next_hex40.r == 0)
        self.assertTrue(next_hex40.s == 0)

        # print(next_hex50)
        self.assertTrue(next_hex50.q == -3)
        self.assertTrue(next_hex50.r == 0)
        self.assertTrue(next_hex50.s == 2)

        # print(next_hex60)
        self.assertTrue(next_hex60.q == 0)
        self.assertTrue(next_hex60.r == 10)
        self.assertTrue(next_hex60.s == 4)

    # `class test_ship
