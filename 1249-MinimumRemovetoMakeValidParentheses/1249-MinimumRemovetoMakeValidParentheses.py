        to_remove = set()

        # identify which parentheses are mismatched
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)

        # removed any unmatched opening parentheses left in stack
        to_remove.update(stack)

        # Construct the final valid string
        result = ""
        for i, c in enumerate(s):
            if i not in to_remove:
                result += c

        return result
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
"
