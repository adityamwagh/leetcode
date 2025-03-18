class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
            
        seen = set()
        l = 0
        substrs = 0
        
        for r in range(len(s)):
            # If we encounter a character already in our window, we need to
            # shrink the window from the left until we remove that duplicate
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            # Add current character to our set
            seen.add(s[r])
            
            # If our window is exactly size k, we found a valid substring
            if r - l + 1 == k:
                substrs += 1
                # Remove leftmost character and advance left pointer
                # to maintain sliding window of size k-1
                seen.remove(s[l])
                l += 1
                
        return substrs