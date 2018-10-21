# 53. Maximum Subarray
"""
Easy  Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

def maxSubArray(A):
    currsum = maxsum = A[0]
    for num in A[1:]:
        currsum = max(num+currsum , num)
        maxsum = max(currsum, maxsum)
    return maxsum

# Time O(N), Space O(2)
