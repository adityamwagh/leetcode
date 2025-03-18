class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        
        l = 0
        used_bits = 0
        longest = 1

        for r in range(len(nums)):
            
            while used_bits & nums[r] != 0:
                used_bits ^= nums[l]
                l += 1
            
            used_bits |= nums[r]

            longest = max(longest, r - l + 1)
        return longest
