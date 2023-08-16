# Solution 1: two pointer
# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        correct_idx = 0
        
        for current_idx in range(1,len(nums)):
            if nums[current_idx] != nums[current_idx-1]:
                correct_idx +=1
                nums[correct_idx] = nums[current_idx]
        return correct_idx+1
        