class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(price - buy_price, profit)

        return profit
