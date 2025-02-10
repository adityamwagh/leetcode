class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c.isalpha():
                stack.append(c)
            elif c.isdigit():
                stack.pop()

        return "".join(stack)