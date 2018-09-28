# 79. Word Search
"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

# DFS
# Time O(N^2) for N*N board, or Time O(M*N) for M*N board.
def exist(self, board, word):
    if not board:  return False
    for i in range(len(baord)):                 # scan in row
        for j in range(len(board[0])):          # scan in column    
            if self.dfs(board, i, j, word):     # DFS search
                return True
    return False
    
def dfs(self, board, i, j, word):
    if len(word) == 0 :  return True            # all characters in word are checked
    if i<0 or i>len(board) \
    or j<0 or j>len(board[0]) \
    or word[0]!=board[i][j] :                   # Edge Cases
        return False
        
    visit = board[i][j]                         # save visit character in temp for later reconstruction. (excluded for only 1 run)
    board[i][j] = '#'                           # avoid visit back again
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(baord, i-1, j, word[1:]) \
    or self.dfs(baord, i, j+1, wor[1:]) or self.dfs(board, i, j-1, word[1:])
    
    board[i][j] = visit                         # update board back to its original value for next run. (excluded for only 1 run)
    
    return res
    



