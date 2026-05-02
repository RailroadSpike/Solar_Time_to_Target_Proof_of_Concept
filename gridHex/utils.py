
# conversion functions to convert between triaxial qrs and cubic xyz coordinates
# given a set of q,r,s cubic coordianes, return x,y,z triax coordinates
# from Ske
def cubic_to_triax(q, r, s):
    if abs(q) >= abs(r) and abs(q) >= abs(s):
        return s, 0, -r
    elif abs(r) >= abs(s):
        return 0, s, q
    else:
        return -q, -r, 0


# given a set f x,y,z cubic coordinates, return triax coordinates
# from Ske
def triax_to_cubic(x, y, z):
    q = -x + z
    r = -y - z
    s = -q - r
    return q, r, s
