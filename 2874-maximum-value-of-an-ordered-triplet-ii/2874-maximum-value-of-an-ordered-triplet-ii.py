class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Greedy by fixing k -> T: O(n) S: O(1)
        # Need to store max value of i, max value of difference
        # and max value of result
        max_value = 0
        n = len(nums)
        max_i, max_diff = 0, 0

        for k in range(n):
            max_value = max(max_value, max_diff * nums[k])
            max_diff = max(max_diff, max_i - nums[k])
            max_i = max(max_i, nums[k])
        return max_value