class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min_price = prices[0]+1
        profit = 0
        for p in prices:
            if p < Min_price:
                Min_price = p
            elif p - Min_price >= profit:
                profit = p-Min_price
        return profit