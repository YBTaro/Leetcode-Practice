# solution 2: DP
# time: O(n)
# space: O(n)
# c(n) = c(n-1)+c(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        if n == 1:
            return dp[0]
        elif n ==2:
            return dp[1]
        else:
            for i in range(2,n):
                dp.append(dp[-1]+dp[-2])
            return dp[-1]

## solution 3:Fibonacci Number
# c(n) = c(n-1)+c(n-2)
# time: O(n)
# space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return a
        elif n ==2:
            return b
        else:
            for i in range(2,n):
                temp = a
                a = b
                b = temp + b
            return b