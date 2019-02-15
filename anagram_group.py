# 49. Group Anagrams
"""
Given an array of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
•	All inputs will be in lowercase.
•	The order of your output does not matter.
"""

# Time O(N); Space O(1)
def groupAnagrams(strs):
    d = {}
    for word in strs:
        d_key = tuple(sorted(word))
        d[d_key] = d.get(d_key,[]) + [word]
    return d.values()




