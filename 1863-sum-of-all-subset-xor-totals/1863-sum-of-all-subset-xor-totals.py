class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xor_sum = 0
        n = len(nums)

        for mask in range(1 << n):
            # compute xor of subset
            xor = 0
            for i in range(n):
                if mask & (1 << i):
                    xor ^= nums[i]
            xor_sum += xor

        return xor_sum
