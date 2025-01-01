# def power(x,y):
#     if y ==0 :
#         return 1
#     if y% 2 == 0:
#         return power(x,y//2) * power(x,y//2)
#     return x * power(x,y // 2) * power(x,y // 2)

# function to calculate order of the number 

def order(x):
    #  variable to store  of the number
    # n =0
    # while(x != 0):
    #     n = n + 1
    #     x = x // 10
    # print(f"order: {n}")

# new way
    if x == 0:
        return 1
    n = len(str(abs(x)))
    return n

# function to check whether the given number is arm or not

def arm(x):
    n=order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + pow(r,n)
        temp = temp // 10

    # if condition satisfies
    return (sum1 == x)

# driver code
x =153

if arm(x) == True:
    print(f"{x} is an armstrong number! ")
else:
    print(f"{x} is not an armstrong!! ")
    