class Solution:
    def toLowerCase(self, s: str) -> str:
        slower = ""
        for c in s:
            if 65 <= ord(c) <= 90:
                c = chr(ord(c) + 32)
            slower += c
        return slower
"
