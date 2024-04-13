class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                product += 1
        return 1 if product % 2 == 0 else -1
[
