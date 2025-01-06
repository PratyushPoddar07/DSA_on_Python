class Solution(object):
    def rotate(self,nums,k):
        """
        Rotate the array to the right by  k steps.

        :type nums: List[int]
        :type k: int 
        :rtype: None(modifies nums in-place)

        """
        n = len(nums)
        k= k% n

        def reverse(start,end):
            while start <end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # step 1:Reverse the entire arrays
        reverse(0,n-1)
        # step 2 :Reverse the first k element
        reverse(0,k-1)
        # rest of element
        reverse(k,n-1)

        return nums


# example usage

if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int,input("Enter array element").split()))
    k = int(input("Enter the rotate: "))
    print(f"Original array: {nums}")
    res = sol.rotate(nums,k)
    print(f"rotated array: {res}")