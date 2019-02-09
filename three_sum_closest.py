# 16. 3Sum Closest  
"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# Time O(N^2), Tow Pointers
def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r :
            sum3 = nums[i] + nums[l] + nums[r]
            if sum3 == target:
                return sum3
            if abs(sum3-target) < abs(sum3-target):
                res = sum3
            if sum_nums < target:
                l += 1
            elif sum_nums > target:
                r -= 1
    return res




