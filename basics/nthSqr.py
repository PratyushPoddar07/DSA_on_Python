def findSqr(n):
    sum =0
    for i in range(1,n+1):
        sum = sum +(i*i)
        
    return sum

num = int(input("Enter the number: "))

print(f"Square upto {num} = {findSqr(num)}")