def SI(p,t,r):
    if(p | t | r  == 0):
        return 0
    si = float(p*r*t)/100
    return si

print(SI(10000,5,5))