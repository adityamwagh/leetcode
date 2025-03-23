class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) < len(goal):
            return False
        
        goal = goal + goal

        for i in range(len(goal) - len(s)):
            if s == goal[i:i+len(s)]:
                return True
        return False