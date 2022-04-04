class Solution:
    
    def myPow(self, x: float, n: int) -> float:
        
#         mag = 1
#         ans = 0.0
        
#         # 1/2 ^ -4
#         if n < 0:
#             for i in range(-n):
#                 mag *= x
            
#             ans = 1 / mag
        
#         else:
#             for i in range(n):
#                 mag *= x
            
#             ans = mag
            
        
#         return ans

# O(n) solution gives TLE

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            # compute x ^ n-1 for odd and x ^ n for even in one step.
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res