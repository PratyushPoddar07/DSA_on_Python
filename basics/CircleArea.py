import math

def area(r):
    # pi = 3.14
    result = round(math.pi * pow(r,2),3)
    return result

print(area(4))