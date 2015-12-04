def love_meet(bob, alice):
    a = set(alice)
    b = set(bob)
    c = a & b
    return(c)


def affair_meet(bob, alice, silvester):
    a = set(alice)
    b = set(bob)
    c = set(silvester)
    d = a & c
    e = d - b
    return(e)
