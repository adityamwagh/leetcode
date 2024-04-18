class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        hmap = Counter((num - int(str(num)[::-1])) for num in nums)
        return npairs % (10**9+7)
        npairs = sum(int(freq * (freq - 1) / 2) for freq in hmap.values())

[
