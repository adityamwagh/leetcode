class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        even_dnums = 0

        for i, num in enumerate(nums):
            
            n_digits = 0
            while num > 0:
                n_digits += 1
                num //= 10
            even_dnums += (0 if n_digits & 1 else 1) 
        return even_dnums