import math
# to check whether a number is in fibo or not : (5*n^2)+4 or (5*n^2)-4
def isPerfectSqr(number):
    s = int(math.sqrt(number))
    return s*s == number

def fibo(num):
    if isPerfectSqr(5*(num**2)+4) or isPerfectSqr(5*(num**2)-4) == True:
        return True
    else:
        return False
    
num = int(input("Enter the number: "))
if fibo(num) == True:
    print(f"{num} is a fibo number.")
else:
    print(f"{num } is not a fibo number.")
    
