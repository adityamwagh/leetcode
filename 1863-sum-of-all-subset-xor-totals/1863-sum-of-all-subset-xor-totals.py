class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # # T: O(2^n): S: O(1)
        # # Create subsets and compute the xor while creating subsets
        # xor_sum = 0
        # n = len(nums)

        # for mask in range(1 << n):
        #     # compute xor of subset
        #     xor = 0
        #     for i in range(n):
        #         if mask & (1 << i):
        #             xor ^= nums[i]
        #     xor_sum += xor

        # return xor_sum

        # T: O(1) S: O(1)
        # Math trick
        # find all the 1 bits places that appear atleast once
        # Each of these will be picked half of the times
        # multiply by 2 ^ (n - 1) => bitshift by n - 1
        ones = 0
        n = len(nums)
        for num in nums:
            ones |= num
        
        xor_sum = ones << (n - 1)
        return xor_sum
