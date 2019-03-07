17. Letter Combinations of a Phone Number
"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is same as phone. 
Note that 1 does not map to any letters.
 
Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, 
your answer could be in any order you want.
"""

# Backtracking. Time O(3^N+4^M); Space O(3^N+4^M). N for digits have 3 letters, M for digits have 4 letters.
def letterCombinations(digits):
    d_l = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
          '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return [a+b for a in d_l.get(digits[0], '')
            for b in letterCombinations(digits[1:])] or ['']




