# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if len(prices) == 0:
            return 0

        max_price: int = prices[-1]
        max_price_day: int = len(prices) - 1

        max_profit: int = 0
        buying_day: int = len(prices) - 1
        selling_day: int = len(prices) - 1

        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
                max_price_day = i
            profit = max_price - prices[i]
            if profit > max_profit:
                max_profit = profit
                buying_day = i
                selling_day = max_price_day

        return max_profit
