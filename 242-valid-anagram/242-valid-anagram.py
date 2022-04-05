from collections import OrderedDict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hm1 = {}
        hm2 = {}
        
        # get count of letters in first string
        for cs in s:
            if cs in hm1:
                hm1[cs] += 1
            else:
                hm1[cs] = 1
        
        # get count of letters in second string   
        for ct in t:
            if ct in hm2:
                hm2[ct] += 1
            else:
                hm2[ct] = 1
        
        # compare hash maps
        if hm1 == hm2:
            return True
        
        return False