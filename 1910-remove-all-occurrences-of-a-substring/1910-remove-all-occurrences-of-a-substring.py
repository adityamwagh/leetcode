class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while (s.find(part) != -1):
            i = s.find(part)
            s = s[:i] + s[i+len(part):]
        return s