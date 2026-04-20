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
    print(f"### Testing {name} ###")
    result = function(*parameters)  # tuple expansion
    print(f"-> {result}")
    print(f'   {answer} targeted')
    message = "PASS ---" if result == answer else "FAIL !!!"
    print(message)
    print("###")


if __name__ == '__main__':
    hex1 = Hex(2, 4, 0)
    hex2 = Hex(-3, 0, 2)

    test(str, (hex1,), "2 , 4 , 0", "hex1.__str__()")
    test(str, (hex2,), "-3 , 0 , 2", "hex2.__str__()")
    print()

    test(str, (hex1.xEuc,), "-1.7320508075688772", "hex1.xEuc.__str__()")
    test(str, (hex1.yEuc,), "5.0", "hex1.yEuc.__str__()")
    test(str, (hex2.xEuc,), "4.330127018922193", "hex2.xEuc.__str__()")
    test(str, (hex2.yEuc,), "-0.5", "hex2.yEuc.__str__()")
    print()

    test(Hex.hexDist, (hex1, hex2), 9, "Hex distance")
    test(Hex.euclidDist, (hex1, hex2), 8.185352771872449, "Euclidian distance")
    print()

    print('end')
