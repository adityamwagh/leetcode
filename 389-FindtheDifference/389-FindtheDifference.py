class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        extra = 0
        for c in s:
            extra ^= ord(c)
        for c in t:
            extra ^= ord(c)
        return chr(extra)

"
