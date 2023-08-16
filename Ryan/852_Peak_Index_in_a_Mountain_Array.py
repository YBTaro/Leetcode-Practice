# solution 1 - linear saearch
# Time: O(n)
# Space: O(1)

# solution 2 - binary search
# Time: O(logn)
# Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l<=r:
            m = (l+r)//2
            if arr[m]<arr[m+1]:
                l = m+1
            elif arr[m]>arr[m+1]:
                if arr[m]>arr[m-1]:
                    return m
                else:
                    r = m-1
        return
        