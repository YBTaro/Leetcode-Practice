# Solution 1: top-down DP
# Time: O(S*n), where S is the amount and n is the denomination of coins. Explain: S subproblems and n times operation for each
# Space: O(S), for dict
#Runtime: 1972 ms, faster than 20.51% of Python3 online submissions for Coin Change.
# Memory Usage: 20.3 MB, less than 13.18% of Python3 online submissions for Coin Change.
class Solution:
    def __init__(self):
        self.dp = dict()
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        return self.helper(coins, amount)
    def helper(self, coins, amount):
        if amount <0:
            return -1
        elif amount == 0:
            return 0            
        elif amount in self.dp:
            return self.dp[amount]
        cpr_set = set()
        for c in coins:
            cpr_set.add(self.helper(coins,amount-c)+1)
        cpr_set.discard(0)
        if len(cpr_set)==0:
            self.dp[amount] = -1
            return -1
        self.dp[amount] = min(cpr_set)
        return self.dp[amount]
        
######################################
# Solution 2: bottom-up DP
# Time: O(S*n), where S is the amount and n is the denomination of coins. Explain: S subproblems and n times operation for each
# Space: O(S), for dict
#Runtime: 1104 ms, faster than 92.19% of Python3 online submissions for Coin Change.
#Memory Usage: 14.3 MB, less than 97.66% of Python3 online submissions for Coin Change.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        elif amount ==0:
            return 0
        dp = [0]
        for a in range(1,amount+1):
            cpr_set = set()
            for c in coins:
                if a-c>=0:
                    cpr_set.add(dp[a-c]+1)
            cpr_set.discard(0)
            if len(cpr_set)==0:
                dp.append(-1)
            else:
                dp.append(min(cpr_set))
        return dp[-1]