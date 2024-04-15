class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        char = ""
        if not s[0].isnumeric() and s[0] in ('-','+'):
            char += s[0]
            s = s[1:]
        for i in s:
            if i.isnumeric(): char+=i
            else: 
                break
        if not char or (len(char) == 1 and char[0] in ('-','+')):
            return 0
        ans = int(char)
        if ans >= 2**31 -1:
            return 2**31 -1
        elif ans <= -2**31:
            return -2**31
        return ans
"
