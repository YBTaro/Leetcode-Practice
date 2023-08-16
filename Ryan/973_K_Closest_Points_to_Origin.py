# Solution 1 - heap
# Time: O(n+klogn)
# Space: O(n)
# Runtime: 676 ms, faster than 64.25% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 20 MB, less than 53.13% of Python3 online submissions for K Closest Points to Origin
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dis = pow(p[0],2)+pow(p[1],2)
            heap.append((dis,p))
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

# solution 2 - quickselect
# Time: O(n) for average, O(n^2) for worst case
# Space: O(1)
# Runtime: 1164 ms, faster than 5.06% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.7 MB, less than 89.04% of Python3 online submissions for K Closest Points to Origin.
class Solution:
    def distanceof(self, p:list[int]):
        return pow(p[0],2)+pow(p[1],2)
    
    def quickselect(self, points, left, right) -> int:
        pivot_ori_idx = random.randint(left, right)
        points[pivot_ori_idx], points[right] = points[right], points[pivot_ori_idx]
        i = left
        for j in range(left, right):
            if self.distanceof(points[j]) <= self.distanceof(points[right]):
                points[i], points[j] = points[j], points[i]
                i+=1
        points[right], points[i] = points[i], points[right]
        return i


    def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
        left = 0
        right = len(points)-1
        while left<right:
            pivot_idx = self.quickselect(points, left, right)
            if pivot_idx == k:
                return points[:k]
            elif pivot_idx > k:
                right = pivot_idx-1
            else:
                left = pivot_idx+1
        return points[:k]

# solution 3 - sort
# Time: O(nlogn)
# Space: O(n)
# Runtime: 624 ms, faster than 93.38% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.6 MB, less than 89.04% of Python3 online submissions for K Closest Points to Origin.
class Solution:
    def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
        if k>=len(points):
            return points
        return sorted(points, key = lambda x: x[0]**2+x[1]**2)[:k]