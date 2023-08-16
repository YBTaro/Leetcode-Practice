# solutioln 1 - brute force
# Time: O(N*K)
# Space: O(1)

# solution 2 - extra space
# Time: O(N)
# Space:O(N)

# Solution 3 - reverse
# Time: O(N)
# Space: O(1)
class Solution:
    def reverse(self, nums, left, right):
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        self.reverse(nums, 0,n-k-1)
        self.reverse(nums, n-k,n-1)
        self.reverse(nums,0,n-1)
        