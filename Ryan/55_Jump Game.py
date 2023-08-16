# solution 0: brute force
# use backtrack, for each node, recursively the nodes it can access, and determine if it can reach the end of array
# Time: O(2^n), since T(x) = T(x+1)+T(x+2)....T(n-1) = 2 T(x+1) = (2^2)*T(x+2) = ... = (2^(x+(n-1-x)))*T(n-1)
# Space: O(n) for recursive

# solution 1: DP, Top-down
# use a array to memorize if the node is good, bad, unknowm, to reduce the time we access nodes.
# time: O(n^2), for every node in array, we are trying to find if it can access a good node -> worse case: n^2
# space: O(n) for dp table

# solution 2: DP, bottom up
# time: O(n^2)
# space: O(n)
# over-time -> not accept
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0]*(len(nums)-1) + [1]
        for i in range(len(nums)-2, -1, -1):
            for jump in range(nums[i],0,-1):
                if dp[min(i+jump,len(nums)-1)]==1:
                    dp[i] = 1
                    break
        return dp[0]


# Here is the 4 steps to understand a dp porblem:
# 1.Start with the recursive backtracking solution
# 2.Optimize by using a memoization table (top-down[2] dynamic programming)
# 3.Remove the need for recursion (bottom-up dynamic programming)
# 4.Apply final tricks to reduce the time / memory complexity

# solution 3: greedy
# time: O(n)
# space: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True

        reach = 0
        for i in range(0,len(nums)-1):
            if i > reach:
                return False
            reach = max(reach, i+nums[i])
            if reach>=len(nums)-1:
                return True
            