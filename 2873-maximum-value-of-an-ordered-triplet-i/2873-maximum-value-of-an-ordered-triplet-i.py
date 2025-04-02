class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        max_value = -float("inf")
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
        return max(max_value, 0)