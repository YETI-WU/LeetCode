# 67. Add Binary
"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""


def addBinary(a,b):
    return bin(eval('0b'+a) + eval('0b'+b))[2:]

# '0b'  means that the number that follows is in binary
# [2:]  to cut of the head "0b" of the binary number





