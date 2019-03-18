# 47. Permutations II
"""
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.
Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


def permutationUnique(nums):
    ans =[[]]
    for num in nums:
        ans = [ l[:i]+[n]+l[i:] for l in ans for i in ...

               
# NOT finished.....

