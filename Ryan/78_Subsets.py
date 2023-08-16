# Soltion 1 - Cascading - orignial version
# Time: O(N*2^N) to generate all subsets and then "copy" them into output list.
# Space:O(N*2^N) :2^N possibilities, and each has at most N element
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            wait_list = []
            for combination in ans:
                new_combination = combination.copy()
                new_combination.append(num)
                wait_list.append(new_combination)
            ans.extend(wait_list)
        return ans
    
# Solution 1 - Cascading - improved version        
# Time: O(N*2^N)
# Space:O(N*2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]        
        for num in nums:
            ans += [curr + [num] for curr in ans]
        return ans

# Solution 2 - Backtrack
# Time: O(N*2^N)
# Space: O(N), for curr list
class Solution:
    def subsets(self, nums:List[int]) -> List[List[int]]:

        def backtrack(idx = 0, curr = []):
            if len(curr)==length:
                ans.append(curr[:])
                return
            elif idx == n:
                return
            curr.append(nums[idx])
            backtrack(idx+1,curr)
            curr.pop(-1)
            backtrack(idx+1,curr)
            
        ans = []
        n = len(nums)
        for length in range(0,n+1):
            backtrack()
        return ans