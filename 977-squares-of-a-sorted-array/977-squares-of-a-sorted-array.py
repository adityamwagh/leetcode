class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        sq_nums = [x*x for x in nums]
        
        return sorted(sq_nums)