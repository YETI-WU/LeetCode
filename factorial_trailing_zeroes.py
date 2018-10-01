# 172. Factorial Trailing Zeroes
"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
"""

# a factorial number with factor 2 & 5 give a trailing zero.
# facotr 2 is plenty; factor 5 is the key

# Recursive 
def factorialTrailingZeroes(self,n):
    if n==0 :  
        return 0
    else:  
        return  n//5 + self.factorialTrailingZeroes(n//5)
    
    
    
    
    
