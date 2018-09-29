# 130. Surrounded Regions
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

def solve(board):
    if not any(board):  return
    
    r , c = len(board) , len(board[0])  # r : row ; c : column
    edgeO = []  # stack to record 'O' location at the edge and linked neighbors
    
    # save all the edge 'O' location into stack edgeO
    for i in range(r):
        if board[i][0]=='O' :  edgeO.append((i,0))          # scan 1st column
        if board[i][c-1]=='O' :  edgeO.append((i,c-1))      # scan last column
    for j in range(c):
        if board[0][j]=='O' :  edgeO.append((0,j))          # scan 1st row
        if board[r-1][j]=='O' :  edgeO.append((r-1,j))      # scan last row

    # mark down edge 'O' to '#' and search neighbors
    while edgeO:
        i , j = edgeO.pop()
        if 0 <= i < r and 0 <= j < c and board[i][j]=='O':
            board[i][j] = '#'   # mark down all NO-flipped 'O' to '#'
            edgeO += (i+1,j) , (i-1,j) , (i, j+1) , (i, j-1)    # Add neighbor location to check 'O'
    
    # flip 'O' to 'X', and flip '#' to 'O'
    for i in range(r):
        for j in range(c):
            if board[i][j]=='#' : board[i][j] = 'O'
            else: board[i][j] = 'X'
            
        
        
    
    
