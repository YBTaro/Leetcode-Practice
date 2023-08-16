# Solution 1 - backtrack
# time: O(N*N!), it takes N step to generate a permutation, and we have N! possible combination.
#                (It's a loose upper bound, but it's fine)
# space: O(N) for hash, O(N) for recursive, O(N) for current candidate, and we ignore the space of ans, which is O(N*N!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_comb = [], cnt = dict()):
            if len(curr_comb)==len(nums):
                ans.append(curr_comb[:])
                return
            for num in cnt:
                if cnt[num]>0:
                    curr_comb.append(num)
                    cnt[num] -=1
                    backtrack(curr_comb, cnt)
                    curr_comb.pop(-1)
                    cnt[num] +=1
        ans = []
        backtrack([],Counter(nums))
        return ans 

