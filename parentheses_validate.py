# 20. Valid Parentheses
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
1.	Open brackets must be closed by the same type of brackets.
2.	Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


# Time O(N); Space O(1)
def validParentheses(s):
    if len(s)%2: return False                           #0# Non-Even, directly exclude
    paren_dic = { '(' : ')' , '[' : ']' , '{' : '}' }   #1# dictionary : open : close
    stack = []                                          #2# stack : last in should first out
    for c in s:
        if c in paren_dic: 
            stack.append(paren_dic[c])                  #3# put needed Close_parenthesis to stack
        elif not stack or c != stack.pop():             #4# have closed_paren, but NO open_paren in stack. or the close_paren NOT match
            return False
    return stack == []




