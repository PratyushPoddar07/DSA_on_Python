num1 = int(input("Enter num1:   "))
num2 = int(input("Enter num2:   "))

# sum = num1+num2

# print(sum)

# --FUNCTION--

# def ADD(num1,num2):
#     return num1+num2

# print(ADD(num1,num2))

# --RECURSIVELY--
def add_recursive(x,y):
    if y ==0:
        return x
    else:
        return add_recursive(x+1,y-1)
    

result = add_recursive(num1,num2)
print(result)
