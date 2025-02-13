class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        iters = 0
        heapq.heapify(nums)
        while (not nums[0] >= k):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            iters += 1
        return iters