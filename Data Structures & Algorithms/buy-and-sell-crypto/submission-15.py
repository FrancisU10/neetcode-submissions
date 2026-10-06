class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = 0
        big = 1
        maximumPrice = 0
        while big < len(prices):
            if prices[small] < prices[big]:
                maximumPrice = max(maximumPrice, prices[big] - prices[small])
                big += 1
            else:
                small = big
                big += 1
        return maximumPrice
