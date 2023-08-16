# Solution 1: greedy
# Time : O(symbol), here symbol = 13, which is a constant, so we can also say O(1)
# space: O(symbol), here symbol = 13, which is a constant, so we can also say O(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        pairs = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"), 
                (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),
                (4,"IV"),(1,"I")]
        
        ans = ""
        for digit, roman in pairs:
            d = num // digit
            if d:
                ans += (roman*d)
                num = num % digit
        return ans
            