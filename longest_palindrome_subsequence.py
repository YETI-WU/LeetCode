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
    
    for cl in range(2, n+1): # start from 2nd to the last
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl ==2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1]+ 2 
            else: 
                L[i][j] = max(L[i][j=1], L[i+1][j])

return L[0][n-1]





