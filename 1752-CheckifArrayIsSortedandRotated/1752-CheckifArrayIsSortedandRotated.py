class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        B = nums
        A = sorted(nums)
        for x in range(n):
            if all(A[i] == B[(i + x) % n] for i in range(n)):
                return True
        return False
