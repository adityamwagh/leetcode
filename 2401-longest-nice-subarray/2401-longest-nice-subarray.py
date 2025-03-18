class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        left = 0
        used_bits = 0  # Track which bits are used in our current window
        max_length = 1  # Minimum nice subarray length is 1
        
        for right in range(n):
            # While the current number has bits that conflict with our window
            while used_bits & nums[right] != 0:
                # Remove the leftmost number's bits
                used_bits ^= nums[left]
                left += 1
            
            # Add current number's bits to our used_bits
            used_bits |= nums[right]
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length