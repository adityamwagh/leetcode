class Solution:
    def maxScore(self, s: str) -> int:

        total_ones = s.count("1")
        left_zeros = 1 if s[0] == "0" else 0
        right_ones = total_ones - (1 if s[0] == "1" else 0)
        max_score = left_zeros + right_ones

        for i in range(1, len(s) - 1):
            if s[i] == "0":
                left_zeros += 1
            else:
                right_ones -= 1

            max_score = max(max_score, left_zeros + right_ones)
        return max_score
