class Solution:
    # def maximumTripletValue(self, nums: List[int]) -> int:
        
    #     max_value = -float("inf")
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len(nums)):
    #                 max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
    #     return max(max_value, 0)

    def maximumTripletValue(self, nums: List[int]) -> int:
        
        max_value = -float("inf")
        i = 0

        for j in range(i, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                nums[i] = max(nums[i], nums[j])
                max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
        return max(max_value, 0)