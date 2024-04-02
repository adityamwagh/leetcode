class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        imap = {}
        for i in range(len(nums)):
            if nums[i] in imap:
                if abs(i - imap[nums[i]]) <= k:
                    return True
            imap[nums[i]] = i
        return False
[
