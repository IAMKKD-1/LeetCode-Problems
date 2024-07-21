class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = max(profit, prices[j] - prices[i])
            else:
                i = j
            j+=1
        return profit