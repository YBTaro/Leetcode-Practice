# Dp
# Time: O(n^2)
# Space: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lr = [(i,i) for i in range(len(s))]
        
        for idx in range(len(s)-1):
            if s[idx]==s[idx+1]:
                lr.append((idx, idx+1))

        while True:
            temp = []
            for l,r in lr:
                if l-1 >= 0 and r+1 < len(s):
                    if s[l-1]==s[r+1]:
                        temp.append((l-1,r+1))
            if len(temp)==0:
                break
            lr = temp.copy()
        l,r = lr[-1]
        return s[l:r+1]
