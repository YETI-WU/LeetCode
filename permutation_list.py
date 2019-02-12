# 46. Permutations 
"""
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

# Recursive: Time O(N^2)
def permuteList(nums):
    return [ [n] + p
            for i, n in enumerate(nums)
            for p in permuteList(nums[:i]+nums[i+1:])
           ] or [[]]


# Library: Itertools
def permuteList(nums):
     return list(itertools.permutations(nums))


# DFS
def permuteList(nums):
    res = []
    dfs(nums, [], res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
    else:
        for i in range(len(nums)):
            dfs(num[:i]+num[i+1:], path+[nums[i]], res)
            
            
            
            
            
            
