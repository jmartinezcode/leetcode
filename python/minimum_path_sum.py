# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes 
# the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    continue
                if i-1<0: #top row
                    grid[i][j] += grid[i][j-1]
                elif j-1<0: #left col
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[rows-1][cols-1]