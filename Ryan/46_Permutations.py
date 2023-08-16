# Solution 1 - backtrack
# time: O(N!)
# space: O(N!), since we have to keep N! solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(curr = []):
            if len(curr)==length:
                ans.append(curr[:])
            for i in range(0,length):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtracking(curr)
                    curr.pop(-1)
        ans = []
        length = len(nums)
        backtracking()
        return ans

# Solution 1 - backtrack - improved version
class Solution:
    def permute(self, nums):
        def backtrack(curr_idx = 0):
            if curr_idx == n:  
                output.append(nums[:])
            for i in range(curr_idx, n):
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
                backtrack(curr_idx + 1)
                nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
        
        n = len(nums)
        output = []
        backtrack()
        return output