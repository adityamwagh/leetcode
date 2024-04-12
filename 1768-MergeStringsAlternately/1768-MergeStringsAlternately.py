class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        lw1, lw2 = len(word1), len(word2)
        i, j = 0, 0
        while i < lw1 and j < lw2:
            merged += word1[i] + word2[j]
        if i < lw1:
            merged += word1[i:]
        if j < lw2:
            merged += word2[j:]
            i += 1
            j += 1


        
        return merged
"
