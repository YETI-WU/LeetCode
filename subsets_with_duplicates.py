# 90. Subsets II
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# Iterative,  Time O(N), Space O(1)
def substedWithDup(nums):
    res = [ [] ]
    nums.sort()
    for num in nums:
        res += [ [num] + item for item in res  if [num]+item not in res]
    return res




