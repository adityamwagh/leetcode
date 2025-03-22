class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        # number of operations would be 
        # the number of distinct non zero elements
        return len(set(nums) - {0}) 