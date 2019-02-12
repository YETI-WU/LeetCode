# 242. Valid Anagram
"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.
"""

def isAnagram(s, t):
    dic_s, dic_t = {}, {}
    for char in s:
        dic_s[char] = dic_s.get(char, 0) + 1
    for char in t:
        dic_t[char] = dic_t.get(char, 0) + 1
    return dic_s == dic_t

