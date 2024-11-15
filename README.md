# DSA_on_Python

1.<!-- Rotate by given input -->
    nums[4] = nums[3] -> [1, 2, 3, 4, 4]
    nums[3] = nums[2] -> [1, 2, 3, 3, 4]
    nums[2] = nums[1] -> [1, 2, 2, 3, 4]
    nums[1] = nums[0] -> [1, 1, 2, 3, 4]
    nums[0] = last      -> [5, 1, 2, 3, 4] ....

                    or
                    
    Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Normalize 𝑘=3%7=3

    Reverse the entire array:
    Before: [1, 2, 3, 4, 5, 6, 7]
    After: [7, 6, 5, 4, 3, 2, 1]

    Reverse the first 𝑘=3 elements:
    Before: [7, 6, 5, 4, 3, 2, 1]
    After: [5, 6, 7, 4, 3, 2, 1]

    Reverse the remaining 𝑛−𝑘=4 elements:
    Before: [5, 6, 7, 4, 3, 2, 1]
    After: [5, 6, 7, 1, 2, 3, 4]
        