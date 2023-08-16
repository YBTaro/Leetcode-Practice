# solution 1 - heap
# Time: O(X+klogX), where X is min(row_num, k)
# Space: O(X) for heap
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix) # row num = col num = n

        MinHeap = [(matrix[r][0],r,0) for r in range(min(row_num,k))]

        # X = min(row_num, k)
        heapq.heapify(MinHeap) # bottom-up -> O(X)

        for i in range(k): # O(k)
            minimum,r,c = heapq.heappop(MinHeap) # O(logX)

            if c+1 < n:
                heapq.heappush(MinHeap, (matrix[r][c+1],r,c+1)) # O(logX)

            if i == k-1:
                return minimum

# Solution - God binary search
# Time: O(NlogN)
# Space: O(1)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        Start, End = matrix[0][0], matrix[n-1][n-1]
                
        while True:
            count = 0
            MaxOfLeft, MinOfRight = Start,End
            FakeMiddle = (Start+End)//2
            r = n
            for c in range(n): # O(N+N) == O(N)
                while r-1>=0 and matrix[r-1][c] > FakeMiddle:
                    r-=1
                MaxOfLeft = max(matrix[r-1][c], MaxOfLeft) if r-1>=0 else MaxOfLeft
                MinOfRight = min(matrix[r][c], MinOfRight) if r<n else MinOfRight
                count += r
            if count ==k or Start==End:
                return MaxOfLeft
            elif count > k:
                End = MaxOfLeft
            elif count < k:
                Start = MinOfRight
            
