class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):
            return False
        goal = goal+goal
        combined_s = s+'#'+goal
        dp = [0]*len(combined_s)
        for i in range(1, len(combined_s)):
            v = dp[i-1]
            while v and combined_s[v]!=combined_s[i]:
                v = dp[v-1]
            dp[i] = v+(combined_s[v]==combined_s[i])
            if dp[i]==len(s):
                return True
        return False