class Solution:
    
#     def getOnes(self, n: int) -> int:
        
#         count = 0
        
#         while n > 0:
#             n = n & (n - 1)
#             count += 1
                
#         return count
    
#     def countBits(self, n: int) -> List[int]:

#         return [self.getOnes(i) for i in range(n + 1)]

    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            
        return dp