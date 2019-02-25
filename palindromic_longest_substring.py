# 5. Longest Palindromic Substring
"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

# Time O(N^2); Space O(1)
def chk(s,l,r):
  while l>0 and r<len(s) and s[l]==s[r]:
    l += 1
    r += 1
    return s[l+1:r]
  
def longestPalindromicSubstring(s):
  res = ''
  for i in range(len(s)):
    # odd 
    tmp = chk(s,i,i)
    if len(tmp) > len(res): 
      res = tmp
    # even
    tmp = chk(s,i,i+1)
    if len(tmp) > len(res):
      res = tmp
  return res




