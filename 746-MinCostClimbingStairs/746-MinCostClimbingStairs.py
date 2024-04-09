class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stack = cost.copy()

        for i in range(2,len(cost)):
            stack[i] += min(stack[i-1],stack[i-2])
        print(stack)
        return min(stack[-1],stack[-2])
[
