# 125. Valid Palindrome
"""
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""


def isPalindrome(s):
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]

# Python filter
def isPalindrome(s):
    s = list( filter(lambda x: x.isalnum(), s.lower()) )
    return s == s[::-1]

# Two Pointers, Time O(N)
def isPalindrome(s):
    l , r = 0 , len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
        


