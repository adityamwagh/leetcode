class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr = 0
        maxx = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            maxx = max(maxx, curr)
        return maxx