class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        return sorted(sorted(arr, key = lambda y: abs(x - y))[:k])
