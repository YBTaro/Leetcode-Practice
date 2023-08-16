# solution 1 - Dutch National Flag Problem 
# Time : O(n)
# space: O(1)
# Runtime: 28 ms, faster than 91.81% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.1 MB, less than 90.58% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums:List[int]) -> None:
        p1 = 0 # right boundary of 0
        p2 = len(nums)-1 # left boundary of 2

        curr = 0
        while curr <= p2:
            if nums[curr]==0:
                nums[p1], nums[curr] = nums[curr], nums[p1]
                p1+=1
                curr+=1
            elif nums[curr]==2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2-=1
            else:
                curr+=1


# solution 2 - cheating
# Time : O(n)
# space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0,0,0
        for num in nums:
            if num == 0:
                red +=1
            elif num == 1:
                white +=1
            else:
                blue +=1
            
        for i in range(len(nums)):
            if red != 0:
                red -=1
                nums[i] = 0
            elif white !=0:
                white -=1
                nums[i] =1
            else:
                blue -=1
                nums[i] = 2
        