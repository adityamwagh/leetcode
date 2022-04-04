class Solution:
    
    def getSumOfSquares(self, n: int) -> int:
        
        dsum = 0
        while n > 0:
            digit = n % 10
            dsum += (digit ** 2)
            n = n // 10
        
        return dsum
    
    
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = self.getSumOfSquares(n)
            if n == 1:
                return True
            
        return False
            