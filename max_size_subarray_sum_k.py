# 325. Maximum Size Subarray Sum Equals k
"""
Medium  Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest) 

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest) 
"""

def maxSubArray(num, k):
    acc = 0
    dic = {0:-1}   # accumulation : index
    result = 0
    for i , num in enuerate(nums):
        acc += num
        if acc not in dic:
            dic[acc] = i
        if acc-k in dic:
            result = max(result, i - dic[acc-k])
    return result

# Time O(N), Space O(N)




