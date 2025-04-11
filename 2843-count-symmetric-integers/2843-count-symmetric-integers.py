class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        n_symmetric = 0
        for n in range(low, high + 1):
            if 9 < n < 100:
                if n % 10 == n // 10:
                    n_symmetric += 1
            
            if 999 < n < 10000:
                left_sum = n // 1000 + (n // 100) % 10
                right_sum = n % 10 + (n // 10) % 10
                if left_sum == right_sum:
                    n_symmetric += 1
        return n_symmetric