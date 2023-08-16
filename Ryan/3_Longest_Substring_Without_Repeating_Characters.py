# solution 1 : sliding window
# time : O(n)
# space: O(n) for hashmap
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        left = 0
        right = 0
        maxlen = 0
        
        for right in range(0, len(s)):
            c = s[right]
            if c in record:
                left = max(record[c]+1, left)
                record[c] = right
            else:
                record[c] = right
            maxlen = max(maxlen, right-left+1)
        return maxlen
                

new:     
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {} # record the position of char
        left, right = 0,0
        maxlen = 0
        for right in range(len(s)):
            c = s[right]
            if c in record:
                left = max(record[c]+1, left)
            maxlen = max(right - left +1, maxlen)
            record[c] = right
        return maxlen