class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            
            cur_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, cur_profit)

        return max_profit