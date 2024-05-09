class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort()
        _sum = happiness.pop()
        for i in range(1, k):
            h = happiness[-1] - i if happiness[-1] - i > 0 else 0
            happiness.pop()
            _sum += h
        return _sum

[
