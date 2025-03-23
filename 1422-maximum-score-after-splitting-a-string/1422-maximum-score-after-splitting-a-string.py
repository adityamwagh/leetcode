class Solution:
    def maxScore(self, s: str) -> int:
        # Count total number of 1s in the entire string
        total_ones = s.count('1')
        
        # Start with a split after the first character
        # Left part has s[0] zeros, right part has all ones minus any 1 in the first position
        left_zeros = 1 if s[0] == '0' else 0
        right_ones = total_ones - (1 if s[0] == '1' else 0)
        max_score = left_zeros + right_ones
        
        # For each possible split point (except the last character)
        for i in range(1, len(s) - 1):
            # Update counts
            if s[i] == '0':
                left_zeros += 1
            else:  # s[i] == '1'
                right_ones -= 1
                
            # Update max score
            max_score = max(max_score, left_zeros + right_ones)
        
        return max_score
