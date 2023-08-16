# Solution 1 - DP
# Time: O(n^2)
# Space: O(n)
# Three steps for DP
# 1. define dp table: dp[i] = the max subsequence when we use num[i] in the end
# 2. define recurrance relation: dp[i] = max(dp[j]+1) for j<i and nums[j]<nums[i]
# 3. define base case: initialize all dp element to 1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
            ans = max(ans, dp[i])
        return ans

# solution 2 - Intelligently Build a Subsequence
# Time: O(n^2)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                for j in range(len(subseq)):
                    if nums[i] <= subseq[j]:
                        subseq[j] = nums[i]
                        break
        return len(subseq)

# solution 3 - improve 2 by binary search
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                l,r = 0, len(subseq)
                while l<r:
                    m = (l+r)//2
                    if nums[i] <= subseq[m]:
                        r = m
                    else:
                        l = m+1
                subseq[l] = nums[i]
        return len(subseq)
        