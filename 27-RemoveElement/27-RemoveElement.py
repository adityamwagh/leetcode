class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, vcount = 0, nums.count(val)
        for right in range(len(nums)):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return len(nums) - vcount
[
