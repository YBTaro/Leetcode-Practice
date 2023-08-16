# solution 0: brute forst
# time: O((m+n)*path)
# space: O(path)
# for each node, recursively call the right and bottom node 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1) 

# solution 1: dp
# time: O(m*n)
# space: O(m*n)
class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        dp = [[1]*n for _ in range(m)]

        for c in range(1,n):
            for r in range(1,m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]

# solution 2: dp improve
# time: O(m*n)
# space: O(min(m,n))
class Solution:
    def uniquePaths(self, m:int,n:int) -> int:
        if m > n:
            m,n = n,m 
        dp = [1]*(m)
        for _ in range(1,n):
            for r in range(1,m):
                dp[r] = dp[r-1]+dp[r]
        return dp[-1]

# solution 3: math
# time: O(min(m,n))
# space: O(1)
# Runtime: 24 ms, faster than 96.36% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.2 MB, less than 84.87% of Python3 online submissions for Unique Paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<n:
            m,n = n,m
        accu = 1
        for i in range(n, m+n-1):
            accu = accu * i
        for i in range(1,m):
            accu = accu // i
        return accu