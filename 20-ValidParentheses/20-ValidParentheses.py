class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in pmap and stack and stack[-1] == pmap[c]:
                stack.pop()
            else:
        return True if not stack else False
                stack.append(c)
            
"
