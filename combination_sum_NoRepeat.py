# 40. Combination Sum II
"""
Medium  Given a collection of candidate numbers (candidates) and a target number (target), 
ind all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
•	All numbers (including target) will be positive integers.
•	The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


def combinationSum2(candidates, target):
    res = []
    candidates.sort()
    dfs(target, 0, [])
    return res
    
def dfs(need, ind, stack):
    if need == 0:
        res.append[stack]
    if need < 0:
        return
    for i in range(ind, len(candidates)):
        dfs(need-candidates[i], i+1, stack+[candidate[i]])

