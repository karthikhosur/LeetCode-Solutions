class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minima= float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i]<minima:
                minima =prices[i]
            if prices[i]-minima > profit:
                profit = prices[i]-minima
        return profit