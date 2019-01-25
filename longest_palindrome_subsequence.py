# 516. Longest Palindromic Subsequence
"""
Given a string s, find the longest palindromic subsequence's length in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


# <ref> https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# A Dynamic Programming based Python program for LPS problem
# Return the length of the longest palindromic subsequence in seq
def lps(str):
  n = len(str)
  # create a table to store results of subproblems
  L = [ [0 for _ in range(n)] for _ in range(n) ]
  
  # strings of length 1 are palindrome of length 1; diagonal
  for i in range(n):
    L[i][i] = 1

