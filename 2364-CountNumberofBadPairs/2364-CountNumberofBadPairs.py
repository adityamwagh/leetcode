class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        For any pair (i,j) where i < j:

        A valid pair means: j - i = nums[j] - nums[i]
        After transformation: nums[i] becomes nums[i] - i
        nums[j] becomes nums[j] - j

        Two positions i and j form a valid pair if:
        (nums[j] - j) = (nums[i] - i)

        The total number of possible pairs where i < j is n choose 2 (n * (n-1) / 2) because:
        For first position (i=0): we can pair with positions 1 to n-1 (n-1 pairs)
        For second position (i=1): we can pair with positions 2 to n-1 (n-2 pairs)
        And so on...
        """
        badPairs = 0
        n = len(nums)
        for k in range(len(nums)):
            nums[k] = nums[k] - k
        
        counts = Counter(nums)
        validPairs = sum(x * (x - 1) // 2 for x in counts.values() if x > 1)
        return n * (n - 1) // 2 - validPairs
