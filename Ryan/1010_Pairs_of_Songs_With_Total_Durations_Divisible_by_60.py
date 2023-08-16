# solution 0 - brute force
# Time: O(n^2)
# Space: O(1)

# solution 1 - fixed size hashmap
# Time: O(n)
# Space:O(1)
# use the hash table to record the frequence

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashtable = collections.defaultdict(int)
        ans = 0
        for t in time:
            remainder = t%60
            if (a:=hashtable.get((60-remainder)%60,0)): # complement = (60-remainder)%60, %60 is for the case 60
                ans+=a
            hashtable[remainder]+=1
        return ans
                
        
