# solution 1 - heapify (min-heap)
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        
        special = {
            1:"Gold Medal",
            2:"Silver Medal",
            3:"Bronze Medal"
        }
        
        NUMS = nums.copy()
        for idx, __ in enumerate(NUMS):
            NUMS[idx] = [NUMS[idx], idx]
        heapq.heapify(NUMS)
        i = 0
        while NUMS:
            _, idx = heapq.heappop(NUMS)
            nums[idx] = special[len(nums)-i] if len(nums)-i<4 else str(len(nums)-i)
            i+=1
        return nums

# solution 1.5 - heapify (max-heap)
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        special = {
            1:"Gold Medal",
            2:"Silver Medal",
            3:"Bronze Medal"
        }
        
        cpy = []
        for i in range(len(nums)):
            cpy.append([nums[i], i])

        heapq._heapify_max(cpy)
        rk = 1
        while cpy:
            val, idx = heapq._heappop_max(cpy)
            nums[idx] = str(rk) if rk > 3 else special[rk]
            rk+=1
        return nums



#import heapq
#listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
#heapq.heapify(listForTree)             # for a min heap
#heapq._heapify_max(listForTree)        # for a maxheap!!
#heapq.heappop(minheap)      # pop from minheap
#heapq._heappop_max(maxheap) # pop from maxheap
#heapq.heappop(minheap)      # pop from minheap
#heapq._heappop_max(maxheap) # pop from maxheap

# solution 2 - sort and hashmap
# Time: O(nlogn)
# space: O(n)

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:

        special = {
            1:"Gold Medal",
            2:"Silver Medal",
            3:"Bronze Medal"
        }

        cpy = sorted(nums, reverse=1)
        hashmap = {}
        for idx, val in enumerate(cpy):
            hashmap[val] = idx+1
        for idx, num in enumerate(nums):
            nums[idx] = str(hashmap[num]) if hashmap[num] > 3 else special[hashmap[num]]
        return nums


