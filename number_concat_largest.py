# 179. Largest Number
"""
Medium  Given a list of non negative integers, 
arrange them such that they form the largest number.
Example 1:
Input: [10,2]
Output: "210"
Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

# Time O(NlogN), Space(N)
class LargeStrConcat
def __lt__(x,y):
    return x+y > y+x

def largestNumber(nums):
    return ''.join( sorted( map(str,nums), key = LargeStrConcat ) ).lstrip('0') or '0'




