class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        diff = abs(arr[1] - arr[0])
        for i in range(len(arr) - 1):
            if abs(arr[i+1] - arr[i]) != diff:
                return False
        return True
        arr.sort()

[
