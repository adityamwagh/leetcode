class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        badPairs = 0
        n = len(nums)
        for k in range(len(nums)):
            nums[k] = nums[k] - k
        
        counts = Counter(nums)
        validPairs = sum(x * (x - 1) // 2 for x in counts.values() if x > 1)
        return n * (n - 1) // 2 - validPairs