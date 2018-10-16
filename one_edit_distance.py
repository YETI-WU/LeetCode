# 161. One Edit Distance
"""
Medium  An edit between two strings is one of the following changes.
1.	Add a character
2.	Delete a character
3.	Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit. 
xpected time complexity is O(m+n) where m and n are lengths of two strings. 
Examples:
Input:  s1 = "geeks", s2 = "geek"
Output: yes	Number of edits is 1
Input:  s1 = "geeks", s2 = "geeks"
Output: no	Number of edits is 0
Input:  s1 = "geaks", s2 = "geeks"
Output: yes	Number of edits is 1
Input:  s1 = "peaks", s2 = "geeks"
Output: no	Number of edits is 2
"""


# Time O(N); Space O(1)
def isOneEditDistance(s1,s2):
    diff = abs(len(s1)-len(s2))
    
    if diff > 1 or s1==s2:  # exclusion
        return False
    
    if diff == 0:  
        return sum([ s1[i] != s2[i] for i in range(len(s1))]) == 1
    
    if len(s1) > len(s2):  
        s1 , s2 = s2 , s1   # put shorter at front
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i:] == s2[i+1:]  # remove i, then check the rest
    return True




