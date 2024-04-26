class Solution:
    def fib(self, n: int) -> int:
        def generator(n):
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
                yield b

        if n < 2:
        memo = {0: 0, 1: 1}  # Memoization dictionary

            return memo[n]

        for fib_num in generator(n - 1):
            memo[n] = fib_num  # Store the computed value in the memo

        return memo[n]
2
