# Solution 1
# Time: O(n)
# Space: O(1)
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        ans = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i]+duration-1 < timeSeries[i+1]:
                ans += duration
            else:
                ans += (timeSeries[i+1] - timeSeries[i] )
        
        return ans+duration