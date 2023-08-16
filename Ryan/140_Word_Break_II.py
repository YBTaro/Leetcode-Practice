# Solution 1 - Bottom up DP
# Time: O(N^2*D*N^2), N^2 for for loop, D for dict size, N^2 for the largest number if sentence in DP
# Space: O(N^2)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = collections.defaultdict(list)
        dp[-1] = [""]
        for i in range(len(s)):
            for j in range(i+1):
                if j-1 in dp and s[j:i+1] in wordDict:
                    for sentence in dp[j-1]:
                        if sentence != "":
                            dp[i].append(sentence+" "+s[j:i+1])
                        else:
                            dp[i].append(s[j:i+1])
        return dp[len(s)-1]