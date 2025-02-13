class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        iters = 0
        heapq.heapify(nums)
        while (not all(num >= k for num in nums)):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, z)
            iters += 1
        return iters