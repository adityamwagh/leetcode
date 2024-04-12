class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nset, n = set(), 0
        for i in range(len(nums)):
            if nums[i] in nset:
                nums[i] = -200
            else:
                nset.add(nums[i])
        
        for right in range(len(nums)):
            if nums[right] != -200:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                n += 1
        left = 0
            else:
        # count and move -200 to the end 
        
        # ans is length of array - count of -200
        return len(nums) - n
[
