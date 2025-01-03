
def findPosition(k,n):
    f1 = 0
    f2 = 1
    i =2
    while i!=0:
        f3 = f1+f2 # 3
        f1=f2 # 2
        f2 =f3 # 3

        if f2%k == 0:
            return n*i
        i += 1 #4
    
    return 

# number whose multiple we want
k = int (input("Enter k value: "))
# multiple we want
n = int (input("Enter n value: "))

print(f"Position of {n}th multiple of  {k} in fibo series is {findPosition(k,n)}")
