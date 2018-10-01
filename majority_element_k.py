# 229. Majority Element II  
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

# Time O(N); Space O(k)
import collections
def majorityElement(nums, k):
    cntr = collections.Counter()
    for n in nums :
    cntr[n] += 1
    if len(cntr) == k :
        cntr -= collections.Counter(set(cntr))        
    cntr = collections.Counter(n for n in nums if n in cntr)
    return [ n for n in cntr if cntr[n] > len(nums)/k ] 
    
    
    
