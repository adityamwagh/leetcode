class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num, count, n, stack = x, 0, 0, []
        while num:
            count += 1
            num //= 10
        div = 10**(count-1) 
        while x:
            val1 = x % 10
            val2 = x // div
            if val1 != val2: return False
            x %= div
            x //= 10
            div //= 100
            print(val1,val2)
            print('s = ',x,'div = ',div)

        return True
1
