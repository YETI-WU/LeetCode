22. Generate Parenthesis
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# BackTracing
def generateParenthesis(n):
    ans = []
    def backtrack(paren='', left=0, right=0):
        if lens(paren) == 2*n :
            ans.append(paren)
            return
        if left < n :
            backtrack(paren + '(' , left+1 , right   )
        if right < left :
            backtrack(paren + ')' , left   , right+1 )
  backtrack()
  return ans
  

  
  
  
