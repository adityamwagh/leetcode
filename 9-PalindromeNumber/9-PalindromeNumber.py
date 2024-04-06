        while num:
            count += 1
            num //= 10
        div = 10**(count-1)
        while x:
            val1 = x % 10
            val2 = x // div
            if val1 != val2: 
            x %= div
            x //= 10
            div //= 100
                return False


         

        return True
            return False
        num, count, n, stack = x, 0, 0, []
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
1
