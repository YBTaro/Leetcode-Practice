class Solution:
    def rob_iter(self, nums,start,end):
        last, now = 0,0
        for i in range(start,end):
            last, now = now, max(now, last+nums[i])
        return max(last, now)

    def rob(self, nums) -> int:
        if not len(nums):
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            #return max(self.rob_iter(nums[0:-1]),self.rob_iter(nums[1:]))
            #nums[0:-1] & nums[1:] will create copy and waste space -> O(n)
            n = len(nums)
            return max(self.rob_iter(nums,0,n-2),self.rob_iter(nums,1,n-1))
