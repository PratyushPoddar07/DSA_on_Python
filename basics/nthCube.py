def cube(n):
    sum =0 

    for i in range(1,n+1):
        sum = sum +(i**3)

    return sum 

num = int(input("Enter the number: "))

print(f"Cube upto {num} = {cube(num)}")