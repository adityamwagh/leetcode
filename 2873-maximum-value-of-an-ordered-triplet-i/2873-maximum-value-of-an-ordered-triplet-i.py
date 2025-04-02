class Solution:
    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     # Brute force -> T: O(n^3) S: O(1)
    #     # Find all valid triplet values and store maximum.
    #     max_value = -float("inf")
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len(nums)):
    #                 max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
    #     return max(max_value, 0)

    # def maximumTripletValue(self, nums: List[int]) -> int:
    #     # Greedy -> T: O(n^2) S: O(1)
    #     # Maximize nums[i] and scan through array for j, k.
    #     # No need to scan for case when nums[i] < nums[j] (negative reward)
    #     max_value = -float("inf")
    #     i = 0

    #     for j in range(i, len(nums) - 1):
    #         for k in range(j + 1, len(nums)):
    #             nums[i] = max(nums[i], nums[j])
    #             print(nums[i], nums[j], nums[k])
    #             max_value = max(max_value, (nums[i] - nums[j]) * nums[k])
    #     return max(max_value, 0)
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Greedy + Prefix Suffix Max Array -> T: O(n) S: O(n)
        # Precompute maximums on either side of index j.
        # Answer will be max(leftmax[j] - nums[j]) * rightmax[j]
        max_value = -float("inf")
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i - 1])
            suffix_max[n - 1 - i] = max(suffix_max[n - i], nums[n - i])
        
        for j in range(1, n - 1):
            curr_value = (prefix_max[j] - nums[j]) * suffix_max[j]
            max_value = max(max_value, curr_value)
        return max(max_value, 0)