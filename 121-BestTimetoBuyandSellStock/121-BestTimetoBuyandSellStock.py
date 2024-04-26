class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = -float("inf")
        while left <= right and right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            elif prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
        
                right += 1
        return profit if profit != -float("inf") else 0
[
