class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        n_operations = 0
        while True:

            if len(set(nums)) == len(nums):
                return n_operations
            nums = nums[3:]
            n_operations += 1
        