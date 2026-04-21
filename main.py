# proof of concept for calculating intercept time to a target in Solar cataphracts
# define a Hex class with q,r,s coordinates

# create functions for determining hex and euclidian distance between hexes
# create functions to calculate travel time based on distance to a hex
# Perhaps try some route optimization

# proof of concept does not include heat management or ship velocity vector.  Assumes ship at rest traveling in a strait line

# import numpy as np  #may be needed for 3d arrays and some math
# import math
# import matplotlib.pyplot as plt  #  may be used in the future to draw our hexes and orbits
# from sympy import symbols # may be used for some symbolic algebra later

from hex import Hex


def test(function, parameters, answer, name):
    exit_code = 0
    message = "### PASS"
    print(f"### Testing {name} ###")
    result = function(*parameters)  # tuple expansion
    print(f'   {answer} targeted')
    print(f"-> {result}")
    if result != answer:
        message = "### FAIL !!!"
        exit_code = 1
    print(message)
    print("###")
    return exit_code


if __name__ == '__main__':
    hex_0 = Hex(0, 0, 0)
    hex_1 = Hex(2, 4, 0)
    hex_2 = Hex(-3, 0, 2)
    hex_3 = Hex(0, 3, 2)
    hex_4 = Hex(-3, -1, 0)
    hex_5 = Hex(0, -1, -1)
    hex_6 = Hex(2, 0, -2)

    hex_0d = Hex(0, 1, 0)
    hex_60d = Hex(0, 0, 1)
    hex_120d = Hex(1, 0, 0)
    hex_180d = Hex(-1, 0, 0)
    hex_240d = Hex(0, -1, 0)
    hex_300d = Hex(0, 0, -1)

    failures = 0

    failures += test(str, (hex_1,), "2 , 4 , 0", "hex1.__str__()")
    failures += test(str, (hex_2,), "-3 , 0 , 2", "hex2.__str__()")
    print()

    failures += test(str, (hex_1.xEuc,), "-1.7320508075688772", "hex1.xEuc.__str__()")
    failures += test(str, (hex_1.yEuc,), "5.0", "hex1.yEuc.__str__()")
    failures += test(str, (hex_2.xEuc,), "4.330127018922193", "hex2.xEuc.__str__()")
    failures += test(str, (hex_2.yEuc,), "-0.5", "hex2.yEuc.__str__()")
    print()

    failures += test(Hex.hexDist, (hex_1, hex_2), 9, "Hex distance")
    failures += test(Hex.hexDist, (hex_0d, hex_0), 1, "Hex distance along vertical axis")
    failures += test(Hex.euclidDist, (hex_1, hex_2), 8.185352771872449, "Euclidean distance")
    failures += test(Hex.euclidDist, (hex_0d, hex_0), 1.0, "Euclidean distance along vertical axis")
    print()

    print(f'{failures} failed tests')
    print('end')
