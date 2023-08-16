# solution 1 - binary search
# Time: O(logn)
# Space:O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] <= nums[r]:
                r = m
            else: # nums[mid] > nums[r]:
                l = m+1
        return nums[l]

# in this question, we are going to find min, but if we want to find max, we have to compare num[m] with num[l]