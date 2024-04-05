class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        i = 1
        while i < len(s):
            i += 1
            if stack and (ord(s[i]) == ord(stack[-1]) + 32 or ord(s[i]) == ord(stack[-1]) - 32):
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)


"
