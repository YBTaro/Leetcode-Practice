# solution 1 : split then binary search
# Time: O(log n)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def PivotSearch(l,r):
            if nums[l]<=nums[r]:
                return 0
            while l<=r:
                m = (l+r)//2
                if nums[m]>nums[m+1]:
                    return m+1
                elif nums[0] <= nums[m]:
                    l = m+1
                else:
                    r = m-1
        
        def BinarySearch(l, r ,target):
            while l <= r:
                m = (l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
        

        pivot = PivotSearch(0,len(nums)-1)
        if nums[0] > target or pivot == 0:
            return BinarySearch(pivot, len(nums)-1, target)
        else:
            return BinarySearch(0, pivot-1, target)

#########
# Solution 2 - one pass binary search
# Need to consider the special case of Binary search
# Time: O(log n)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = (l+r)//2

        while l<=r:
            if nums[m]==target: # find it
                return m
            elif nums[m]>nums[r]: # middle is in normal array
                if nums[l]<=target and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m]<nums[r]: # middle is in rotated array
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif nums[m]==nums[r]:
                break
            m = (l+r)//2
        return -1
