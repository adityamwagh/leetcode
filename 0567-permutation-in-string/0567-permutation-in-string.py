class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m2 = defaultdict(int)    
        m1 = defaultdict(int)
        for c in s1:
            m1[c] += 1
    
        k = len(s1)
        l = 0

        for r in range(len(s2)):
            
            # if we find a char in s2 that's in s1  
            # then add it to map to compare maps later 
            if s2[r] in m1:

                m2[s2[r]] += 1
                if (r - l + 1) == k:
                    if m2 == m1:
                        return True

                    
                    else:
                        m2[s2[l]] -= 1
                        if m2[s2[l]] == 0:
                            m2.pop(s2[l])
                        l += 1
            else:
                l = r + 1
                m2.clear()

        return False
