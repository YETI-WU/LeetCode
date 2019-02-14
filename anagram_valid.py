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



def isAnagram(s, t):
    return sorted(s) == sorted(t)


"""
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
def isAnagram(s, t):
    lst_s, lst_t = [0] * 26, [0] * 26  # use list's index to represent 26 characters
    for char in s:
        lst_s[ord(char)-ord('a')] += 1  # use ord() to convert unicode character to integer, represent 26 characters
    for char in t:
        lst_t[ord(char)-ord('a')] += 1
    return lst_s.sort() == lst_t.sort()  # use .sort() not sorted() to save space


