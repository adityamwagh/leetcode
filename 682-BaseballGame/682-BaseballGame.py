class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation.isnumeric() or operation.startswith("-"):
                stack.append(int(operation))
            elif operation == "C":
                if stack:
                    stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
[
