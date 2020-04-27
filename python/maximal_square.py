# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

#rows = m
#cols = n

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
         if not matrix or not matrix[0]:
            return 0   

        n, m = len(matrix), len(matrix[0])
        grid = [[0]*(m+1) for x in range(n+1)]  #new grid for dp

        for i in range(n):
            for j in range(m):
                if matrix[i][j] = '1':
                    grid[i][j] = min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1]) + 1
                else:
                    0
                    
        return max([max(m) for m in grid]) ** 2

        