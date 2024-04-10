class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # find max element and it's index
        for i in range(len(nums)):
        for num in nums:
            if nums[i] > m:
                m = nums[i]
                maxIndex = i
            if num != m:
                if m < 2*num:
                    return -1

        return maxIndex
        
        m, maxIndex = -1, -1
                # atleast twice as big
        # check if max element is valid
            
[
