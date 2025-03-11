class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        counts = defaultdict(int)
        substrs = 0

        l = 0
        for r in range(len(s)):

            counts[s[r]] += 1
            while len(counts) >= 3:
                substrs += (len(s) - r) 

                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    counts.pop(s[l])
                l += 1
        return substrs