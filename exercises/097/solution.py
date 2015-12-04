def love_meet(alice, bob):
    a = set(alice)
    b = set(bob)
    c = a & b
    return(c)


def affair_meet(alice, bob, silvester):
    a = set(alice)
    b = set(bob)
    c = set(silvester)
    d = a & c
    e = d - b
    return(e)
