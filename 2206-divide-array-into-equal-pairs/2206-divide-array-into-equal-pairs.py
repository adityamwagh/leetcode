class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)

        for vals in c.values():
            if vals % 2 != 0:
                return False
        return True