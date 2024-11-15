# "Rotate array by given input"

arr = [1,2,3,4,5]
k = int(input("Enter the rotate move: "))

def rotate(nums,int) -> None:
    n = len(nums)
    for _ in range(k):
        last = nums[-1]
        for i in  range(n-1,0,-1):
            nums[i] = nums[i-1]
        nums[0] =last
    return nums

print(rotate(arr,2))