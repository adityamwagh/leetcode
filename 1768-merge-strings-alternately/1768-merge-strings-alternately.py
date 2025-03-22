class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Use zip to pair characters from both words
        merged = ''.join(a + b for a, b in zip(word1, word2))
        
        # Add any remaining characters from the longer word
        # This works because slicing with an index >= len(string) returns an empty string
        remaining_length = max(len(word1), len(word2))
        merged += word1[len(word2):] + word2[len(word1):]
        
        return merged