# Solution 1 - sort and return
# Time: O(N*logN)
# Space: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

# Solution 2 - min Heap
# Time: O(N*logk)
# Space:O(k) for the heap
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


# Solution 3 - quick select
# Time: O(N) in average case, O(N^2) in worst case
# Space: O(1)
class Solution:
    def findKthLargest(self, nums, k):
        def partition(nums, pivot_position, left, right): #-> int
            nums[pivot_position], nums[right] = nums[right], nums[pivot_position]
            i,j = left, left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
            nums[right], nums[i] = nums[i], nums[right]
            return i
        
        n = len(nums)
        left = 0
        right = n-1
        while True:
            pivot_position = partition(nums, random.randint(left, right) , left,right)
            if pivot_position == n-k:
                return nums[pivot_position]
            elif pivot_position < n-k:
                left = pivot_position+1
            else:
                right = pivot_position-1
                
            
