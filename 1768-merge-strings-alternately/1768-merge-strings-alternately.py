class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        
        # Pre-allocate a list with the exact final size needed
        result = [''] * (len1 + len2)
        
        # Fill alternating positions (faster than concatenation)
        for i in range(min_len):
            result[i*2] = word1[i]
            result[i*2+1] = word2[i]
        
        # Handle remaining characters in a single operation (if any)
        if len1 > min_len:
            result[min_len*2:] = word1[min_len:]
        elif len2 > min_len:
            result[min_len*2:] = word2[min_len:]
        
        # Join once at the end (much faster than repeated concatenation)
        return ''.join(result)