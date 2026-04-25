class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy, r = sell
        l, r = 0, 1
        maxProfit = 0

        # Until r is out of bound
        while r < len(prices):
            # 2 3
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

