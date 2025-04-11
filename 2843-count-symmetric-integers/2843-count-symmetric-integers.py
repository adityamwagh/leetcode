class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def is_symmetric(n):
            i = 0
            digits = []
            while n > 0:
                digit = n % 10
                digits.append(digit)
                n //= 10
            print(digits)
            if len(digits) % 2 != 0:
                return False
            
            return sum(digits) / 2 == sum(digits[:len(digits) // 2])
        
        n_symmetric = 0
        for i in range(low, high + 1):
            if is_symmetric(i):
                n_symmetric += 1
        
        return n_symmetric
