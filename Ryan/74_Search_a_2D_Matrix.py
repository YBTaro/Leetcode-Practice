# solution 1
# Time: O(log(mn))
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l,r = 0, row*col-1
        while l <= r:
            m = (l+r)//2
            mrow, mcol = m//col, m%col
            
            middle_val = matrix[mrow][mcol]
            
            if middle_val == target:
                return True
            elif middle_val < target:
                l = m+1
            else:
                r = m-1
        return False
        