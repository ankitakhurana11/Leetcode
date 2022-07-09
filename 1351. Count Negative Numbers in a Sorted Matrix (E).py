Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        i = 0
        j = 0
        cnt = 0
        while i < len(grid) and j < len(grid[0]):
            if grid[i][j] < 0:
                cnt= cnt+1
            if j == len(grid[0])-1:
                i = i+1
                j = -1
            j = j+1
            
        return cnt