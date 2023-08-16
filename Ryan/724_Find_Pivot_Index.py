# solution 1 - brute force
# Time: O(n^2)
# Space: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        return -1

# solution 2 - accumulate
# Time: O(n)
# Space: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        right = total - nums[0]
        for i in range(len(nums)):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1] if i+1 < len(nums) else 0
        return -1
            
# solution 2 - official versiuon
# Time: O(n)
# Space: O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == (total - left - nums[i]):
                return i
            left += nums[i]
        return -1