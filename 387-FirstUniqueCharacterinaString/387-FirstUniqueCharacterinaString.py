class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
        fmap = Counter(s)
            if fmap[s[i]] == 1:
                return i
        return -1
"
