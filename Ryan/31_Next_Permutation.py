# Solution 1 - brute forse - find out all possible and use the order
# time:O(n!)
# space:O(n)

#Solution 2 - one pass
# time: O(n)
# space:O(1)
# Notice: the input may contain same element, such as [5,1,1]
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """ Do not return anything, modify nums in-place instead. """
        j = len(nums)-1

        while j-1!=-1:
            if nums[j-1] >= nums[j]:
                j-=1
            else:
                break
        
        if j-1 == -1:
            nums.reverse()
        else:
            i = len(nums)-1
            while nums[j-1] >= nums[i] and i!=-1:
                i-=1
            nums[j-1], nums[i] = nums[i], nums[j-1]
            #nums = nums[0:j-1]+nums[-1:j-1:-1]  # why not work???
            nums[j:]= nums[-1:j-1:-1]            
        return
        