from math import sqrt
def check(x):
    flag =0

    if (x >1 ):
        for i in range(2,int(sqrt(x))+1):
            if(n%i == 0):
                flag =1
                break
        
        if(flag == 0):
            print("True")
        else:
            print("False")
    else:
        print("False")


n = int (input("Enter the number: "))

check(n)