class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # subtract the sum of n natural numbers from the sum of given array.
        # n is the number of elements in the array.
        n = len(nums)
        
        return int((n * (n + 1) / 2)  - sum(nums))