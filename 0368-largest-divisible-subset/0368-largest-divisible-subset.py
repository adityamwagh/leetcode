# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
#         # Need to find elements that occur as multiples
#         nums.sort()
#         n = len(nums)
#         # store the longest subset starting at i including nums[i]
#         # dp = [[num] for num in nums]
#         dp = [0] * n
#         for i in range(n - 1, -1, -1):
#             for j in range(i + 1, n):
#                 if nums[j] % nums[i] == 0:
#                     dp[i] = max(dp[i], 1 + dp[j])
#                 else:
#                     dp[i] = 1
        
#         return max(dp)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        nums.sort()
        n = len(nums)
        
        # dp[i] stores the length of the largest divisible subset ending with nums[i]
        dp = [1] * n
        
        # prev[i] stores the previous index in the largest divisible subset ending with nums[i]
        prev = [-1] * n
        
        max_length = 1
        max_index = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            # Update the index of the largest subset we've found so far
            if dp[i] > max_length:
                max_length = dp[i]
                max_index = i
        
        # Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        # The result is constructed in reverse order, so we need to reverse it
        return result[::-1]

