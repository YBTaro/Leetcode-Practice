# Solution 0: brute force
# use backtrack
# time: O(2^(m+n)), m,n are the length of row and column
# space: O(m+n) for recursive

# solution 1: dp - 2 dimension
# time : O(m*n)
# space: O(m*n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Grid = grid
        ROW = len(Grid)
        COL = len(Grid[0])
        for r in range(ROW):
            for c in range(COL):
                if r==0 and c==0:
                    continue
                top = Grid[r-1][c] if r-1>=0 else 1000
                left = Grid[r][c-1] if c-1>=0 else 1000
                Grid[r][c] = Grid[r][c] + min(top,left)
        return Grid[-1][-1]

# solution 2: dp - 1 dimension
# time: O(m*n)
# space: O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        window = grid[0]
        ROW = len(grid)
        COL = len(grid[0])

        for r in range(ROW):
            for c in range(COL):
                if r==0 and c==0:
                    continue
                top = window[c] if r-1>=0 else 1000
                left = window[c-1] if c-1>=0 else 1000
                window[c] = grid[r][c] + min(top,left)
        return window[-1]