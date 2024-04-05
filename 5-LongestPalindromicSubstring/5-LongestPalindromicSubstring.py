        x = len(s)
        res = ''
        max_len = 0
        for i in range(x-1,-1,-1):
            for j in range(x-1,i-1,-1):
                # print('checking : ',s[i:j+1])
                # print('cur max : ', max_len, 'res : ',res)
                if j - i + 1 <= max_len: break 
                if s[i:j+1] == s[i:j+1][::-1]: 
                    max_len =  j-i+1
                    res = s[i:j+1]
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:

"
