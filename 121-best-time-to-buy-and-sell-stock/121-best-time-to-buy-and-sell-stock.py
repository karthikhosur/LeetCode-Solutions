class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima= prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i]<minima:
                minima =prices[i]
            if prices[i]-minima > profit:
                profit = prices[i]-minima
        return profit