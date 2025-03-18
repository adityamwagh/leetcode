class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        seen = set()
        l = 0
        substrs = 0
        for r in range(len(s)):

            # If we encounter a character already in our window, we need to
            # shrink the window from the left until we remove that duplicate
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])

            if r - l + 1 == k:
                substrs += 1
                seen.remove(s[l])
                l += 1

        return substrs

