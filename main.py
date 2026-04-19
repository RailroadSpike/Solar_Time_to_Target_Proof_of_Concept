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




if __name__ == '__main__':
    hex1 = Hex(2, 4, 0)
    hex2 = Hex(-3, 0, 2)

    # 2 , 4 , 0
    print(hex1)
    print("\n")
    # -3 , 0 , 2
    print(hex2)
    print("\n")

    # -1.7320508075688772 , 5.0
    print(hex1.xEuc, ',', hex1.yEuc)
    print("\n")
    # 4.330127018922193 , -0.5
    print(hex2.xEuc, ',', hex2.yEuc)
    print("\n")

    # 9
    print("hex distance between hexes is: ")
    print(Hex.hexDist(hex1, hex2))
    print("\n")

    # 8.185352771872449
    print("Euclidian distance between hexes is: ")
    eDistance = Hex.euclidDist(hex1, hex2)
    print(eDistance)

    print('end')
