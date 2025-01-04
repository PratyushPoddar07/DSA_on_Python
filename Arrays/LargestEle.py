def findMax(arr):
    max = -1

    for i in arr:
        if max < i :
            max  = i 


    return max 
arr = {10,20,4}
print(f"max: {findMax(arr)}")        


# one more trick
def largest(arr):
   ans = max(arr)
   return ans

if __name__ == '__main__':
    arr2 = list(map(int,input("Enter the element by space: ").split()))
    n= len(arr2)
    print(f"Largest element is: {largest(arr2)} having {n} element")