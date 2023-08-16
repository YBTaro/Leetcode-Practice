# solution 1 - dp
# Time: O(N^2)
# Space: O(N)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1,1]
        for i in range(2,n+1):
            a = 0
            for left in range(0,(i+1)//2):
                right = i-1-left
                a+=(2*dp[right]*dp[left]) if right!=left else dp[right]*dp[left]
            dp.append(a)
        return dp[n]

# solution 2 - Mathematical Deduction
# Time: O(n)
# Space: O(1)