class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        longest = 0
        e = 0
        while e < len(nums):
            if nums[e] % 2 == 0:
                s=e
                if nums[s]<=threshold:
                    longest = max(longest, 1)
                while (
                    s < len(nums)-1
                    and nums[s] <= threshold
                    and nums[s+1]<=threshold
                    and nums[s+1] % 2 != nums[s] % 2
                ):
                    s += 1
                    longest = max(longest, s - e+1)
                e=s+1
            else:

                e+=1
        return longest
