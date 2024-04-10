class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            i = nums.index(original)
            original = 2*nums[i]
        return original
[
