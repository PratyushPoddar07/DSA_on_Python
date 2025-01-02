from math import sqrt

def prime(n , itr):
    # base case
    if itr == 1 or itr == 2:
        return True
    if n % itr == 0:
        return False
    # recursive function call

    if prime(n,itr-1) == False:
        return False
    return True

num = int(input("Enter the number: "))

itr = int(sqrt(num)+1)

print(prime(num,itr))