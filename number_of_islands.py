# 200. Number of Islands  
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""

# DFS
# Time O(V+E), Vertex and Edge
def numIslands(self, grid):
    if not grid :  return 0
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if gird[i][j] == '1' :
                self.dfs(grid, i, j)
                count += 1
                
    def dfs(self, grid, i, j):
        if i<0 or i>=len(grid) \
        or j<0 or j>=len(gird[0]) \
        or grid[i][j]!='1' :
            return
            
        grid[i][j] = '#'                    # avoid visit back again
        self.dfs(grid, i+1 , j   )
        self.dfs(grid, i-1 , j   )
        self.dfs(grid, i   , j+1 )
        self.dfs(grid, i   , j-1 )
        
        
        
        
        
        
        
        
