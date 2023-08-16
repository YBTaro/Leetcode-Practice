nums = [2,7,9,3,1,9]
100 1 2 20
#sulition1 :iterative (bottom-up), time O(n), space O(1)
class Solution:
	def rob(self, nums) -> int:
		last, now = 0,0
		for money in nums:  # money of now+1 house
		    last, now = now, max(last+money, now)
		return now

------

#sulition of recursive (top-down), time O(n), space O(n)
class Solution:
    def __init__(self):
        self.dp={}
        
    def rob_rec(self, nums, now):
        if now < 0:
            return 0

        if now in self.dp:
            return self.dp[now]

        self.dp[now] = max(self.rob_rec(nums,now-1), nums[now] + self.rob_rec(nums,now-2))
        return self.dp[now]

    def rob(self, nums) -> int:
        return self.rob_rec(nums,len(nums)-1)

-------


#sulition of recursive 2 (top-down), time O(n), space O(n)
class Solution:
    def __init__(self):
        self.dp = {}

    def rob_rec(self, nums, now):
        if now >= len(nums):
            return 0

        if now in self.dp:
            return self.dp[now]

        self.dp[now] = nums[now] + max(self.rob_rec(nums, now+2), self.rob_rec(nums, now+3))
        return self.dp[now]

    def rob(self, nums) -> int:
        return max(self.rob_rec(nums, 0), self.rob_rec(nums, 1))