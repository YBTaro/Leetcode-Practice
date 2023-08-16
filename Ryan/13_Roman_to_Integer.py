# solution 1 - greedy
# Time: O(N)
# Space: O(1) for table
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = collections.OrderedDict({
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        })
        ans = 0
        for i in range(len(s)):
            c = s[i]
            c1 = s[i+1] if i+1<=len(s)-1 else 'I'
            if dic[c] < dic[c1]:
                ans -=dic[c]  # we can also do ans = ans - dic[c] + dic[c1] and i+=2
            else:
                ans += dic[c]
        
        return ans
        
        