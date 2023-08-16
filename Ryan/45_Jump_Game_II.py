# solution 1: dp - bottom up
# time: O(n^2)
# space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0]
        for i in range(len(nums)-2, -1, -1):
            furtherstep = min(nums[i], len(nums)-1-i)
            step = min(dp[-1:-1-furtherstep:-1]+[10001])+1
            dp.append(step)
        return dp[-1]

# solution 2: greedy:
# time: O(n)
# space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_step = 0
        curr_jump_end = 0
        farthest = 0
        for i in range(0, len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i==curr_jump_end:
                curr_jump_end = farthest
                jump_step +=1
        return jump_step