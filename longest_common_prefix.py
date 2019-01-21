# 14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs):
    if not strs:  return ""
    for i, group in enumerate(zip(*strs)):
        if len(set(group)) > 1:
            return strs[0][:i]
        else:
            return min(strs)
"""
list(zip(*["flower","flow","flight"]))
Out: [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
"""
        
        
# use Python Library 
def longestCommonPrefixLib(strs):
    
        
