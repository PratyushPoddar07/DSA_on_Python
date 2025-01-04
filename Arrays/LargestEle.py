def findMax(arr):
    max = -1

    for i in arr:
        if max < i :
            max  = i 


    return max 
arr = {10,20,4}
print(f"max: {findMax(arr)}")        
