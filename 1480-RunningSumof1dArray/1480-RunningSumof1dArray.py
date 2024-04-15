class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefs = [0] * (len(nums))
        for i in range(1, len(nums)):
            prefs[i] = prefs[i-1] + nums[i]
        
        prefs[0] = nums[0]
        return prefs
[
