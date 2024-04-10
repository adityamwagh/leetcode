class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        npairs = 0
            for j in range(i+1, len(nums)):
                if i < j and nums[i] == nums[j] and (i * j) % k == 0:
        for i in range(len(nums)):
                    npairs += 1
        return npairs
[
