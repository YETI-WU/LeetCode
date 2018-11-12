# 397. Integer Replacement
"""
Medium  Given a positive integer n and you can do operations as follow:
1.	If n is even, replace n with n/2.
2.	If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:  8
Output:  3
Explanation:
8 -> 4 -> 2 -> 1

Example 2:
Input:  7
Output:  4
Explanation:
7 -> 8 -> 4 -> 2 -> 1  or
7 -> 6 -> 3 -> 2 -> 1
"""

# Recursive: Time O(logN), Space O(1)
def integerReplacement(n):
    if n==0: 
        return 0
    if n%2:
        reuturn 1 + min(integerReplacement(n-1), integerReplacement(n+1))
    else:
        return 1 + integerReplacement(*n/2)
    
    
# Memoi-zation
def recMemo(n, memo):
    if n in memo:
        return memo[n]
    if n%2:
        memo[n] = 1 + min(recMemo(n+1,memo), recMemo(n-1,memo))
        return memo[n]
    else:
        memo[n] = 1 + recMemo(n/2,memo)
        return memo[n]

def integerReplacmentM(n):
    memo = {1:0}
    return recMemo(n,memo)





