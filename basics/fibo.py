# f(n) = F(n-1) + F(n-2), F(1) =1 , F(2) =1
# f(n) = (1+sqrt(5))^n - (1-sqrt(5))^n / 2^n * sqrt(5)

from math import sqrt

def nthfibo(n):
    res = (((1+sqrt(5))**n ) - ((1-sqrt(5))**n )) / (2**n * sqrt(5))

    print(f"{int(res)} is {n}th fibonacci number")

nthfibo(12)


