# 39. Combination Sum
"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
•	All numbers (including target) will be positive integers.
•	The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(target, [])
    
    def dfs(need, stack):
        if need == 0:
            res.append(stack)
            return
        if need < 0:
            return
        for num in candidates:
            dfs(need-num, stack+[num])
    
    return res
    
# not working, need to contine

