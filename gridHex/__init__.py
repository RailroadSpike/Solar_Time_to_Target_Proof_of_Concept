from .gridHex import Hex


# given two hex objects CURRENT and PREVIOUS, take their difference and then sum the difference with CURRENT
def get_next_hex(current_hex, previous_hex):
    diff_x = current_hex.x - previous_hex.x
    diff_y = current_hex.y - previous_hex.y
    diff_z = current_hex.z - previous_hex.z

    sum_x = current_hex.x + diff_x  # sum difference with the current hex
    sum_y = current_hex.y + diff_y
    sum_z = current_hex.z + diff_z

    return Hex.init_via_cube_cords(sum_x, sum_y, sum_z)  # initialize next hex and return it
