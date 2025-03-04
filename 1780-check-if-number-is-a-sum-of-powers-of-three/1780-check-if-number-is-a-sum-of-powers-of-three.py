class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        seen = set()
        def get_pow(x):
            num, p = x, 0
            while num > 0:
                p += 1
                num //= 3
            p -= 1
            return p
        p = get_pow(n)
        num = n
        while p >= 0 and num >= 0:
            if p not in seen:
                num -= 3**p
                seen.add(p)
                p = get_pow(num)
            else:
                return False
        return True
        

