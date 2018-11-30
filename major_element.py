# 169. Majority Element
"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""

# Time O(N); Space O(N)
import collections
def majorElement(nums):
    cnts = collections.Counter(nums)
    return max(cnts.keys(), key=conts.get)

# Time O(N); Space O(1)
def majorElement(nums):
    major_num = 0
    cnt = 0
    for num in nums:
        if cnt == 0:
            major_num = num
        if major_num != num:
            cnt -= 1
        else:
            cnt += 1
    return major_num
# Boyer–Moore Majority Vote Algorithm
# https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
