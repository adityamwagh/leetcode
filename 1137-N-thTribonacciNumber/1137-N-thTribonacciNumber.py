        # memo[1] = 1
        # memo[2] = 1
        # for i in range(3, n+1):
        #     memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        # return memo[n]
        
        # # O(1) space, O(n) time
        if n == 0:
            return 0
        m1, m2, m3 = 0, 1, 1
        for i in range(3, n+1):
            mN = m1 + m2 + m3
        # # bottom up dynamic programming
        if n == 1 or n == 2:
            return 1
        
            m1 = m2
            m2 = m3
            m3 = mN
        return mN
        #     return n
        # memo = [0] * (n + 1)
4
