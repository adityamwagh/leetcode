class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        # number of operations would be 
        # the number of distinct non zero elements
        return len(set(x for x in nums if x  > 0))
