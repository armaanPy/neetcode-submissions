class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = buy, r = sell
        # loop through prices
        #   if l < r: take profit and increment l
        # else set l to r

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
