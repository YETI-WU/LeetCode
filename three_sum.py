# 15. 3Sum  
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# Time O(N^2), Space O(1)
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):  # len(nums)-2 is because we need at least 3 numbers to continue
        if i > 0 and num[i] == num[i-1]:  # prevent checking duplicate again
            continue  # reject the remaining statement, go back to the top of loop 
        l , r = i+1 , len(nums)-1
        while l < r :
            sum = nums[i] + nums[l] + num[r]
            if sum < 0 :
                l += 1
            elif sum > 0 :
                r -= 1
            else:
                res.append((num[i],num[l],num[r]))
                while l < r and num[l] == num[l+1]:  l += 1  # skip repeating l
                while l < r and num[r] == num[r-1]:  r -= 1  # skip repeating r
                l += 1  ;  r -= 1  # looping forward for differe l and r combination with the same i
    return res

  
  
