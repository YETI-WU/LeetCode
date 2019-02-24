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




