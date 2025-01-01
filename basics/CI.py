def CI(p,r,t):
    if(p == 0):
        return 0
    elif(t == 0):
        return 1
    amt = p*(pow((1 + r/100),t))
    ci = float(amt - p)
    return round(ci,3)

print(CI(3000,5,3))
