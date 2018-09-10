# two_sum.py
"""
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Time O(N); Space O(N)
def twoSum(nums,target):
    if len(nums)<2:
        return False
    
    d = {}    
    for i , num in enumerate(nums):
        need = tareget - num
        if need in d:
            return [i, d[need]]
        else:
            d[num] = i

