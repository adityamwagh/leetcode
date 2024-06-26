class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, count = 0, 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                count += 1
        return count
[
