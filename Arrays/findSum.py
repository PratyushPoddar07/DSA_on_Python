def Sum(arr):
    sum =0

    for i in arr:
        sum = sum +i

    return sum

# arr = [1,2,3]
if __name__ == "__main__":
    # input values for the array in single lines
    arr =list(map(int,input("Enter elements separated by space: ").split()))
    print("Array: ",arr)
    
    # input values for array in multiple lines
    # n = int(input("Enter the number of element length: "))
    # arr2 = []
    # for i in range(n):
    #     element = int(input("Enter the element: "))
    #     arr2.append(element)
    # print(arr2)

print(f"Sum = {Sum(arr)}")