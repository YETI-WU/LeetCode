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
    if len(s)%2: return False
    paren_dic = { '(' : ')' , '[' : ']' , '{' : '}' }
    stack = []
    for c in s:
        if c in paren_dic: stack.append(paren_dic[c])
        elif not stack or c != stack.pop(): return False
    return stack == []

