# 53. Maximum Subarray
"""
Easy  Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

# Time O(N), Space O(2)
def maxSubArray(A):                         #0# edge case
    currsum = maxsum = A[0]                 #1# set initial: current_sum & max_sum
    for num in A[1:]:                       #2# loop through A
        currsum = max(num+currsum , num)    #3# compare current num with current_sum+num
        maxsum = max(currsum, maxsum)       #4# update max_sum 
    return maxsum


