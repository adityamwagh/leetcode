class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache
        def backtrack(i):

            if i >= len(questions):
                return 0
            
            points, brainpower = questions[i]

            return max(
                backtrack(i + 1), # skip
                points + backtrack(i + 1 + brainpower) # take
            )
        
        return backtrack(0)
