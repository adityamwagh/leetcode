class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first decreasing element from right to left
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:  # If we found a decreasing element
            # Find the element just larger than nums[i]
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
                
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the subarray after position i
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1