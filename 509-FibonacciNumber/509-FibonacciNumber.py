class Solution:
    def fib(self, n: int) -> int:
        def generator(n):
            a, b = 0, 1
            yield a
            yield b
            for _ in range(2, n+1):
                a, b = b, a + b
                yield b
        return list(generator(n))[-1]
2
