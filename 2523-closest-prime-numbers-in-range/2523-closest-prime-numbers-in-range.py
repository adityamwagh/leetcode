class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        is_prime = [1] * (right - left + 1)
        primes = []
        result = [-1, -1]
        min_diff = float("inf")

        # case when range starts from 1
        if left == 1:
            if right <= 2:
                return result
            if right > 2:
                return [2, 3]
        
        # find all primes in range
        for k in range(left, right + 1):
            for i in range(2, math.ceil(math.sqrt(k)) + 1):
                if k % i == 0:
                    is_prime[k - left] = 0
                    break
        
        # collect all primes
        for i, flag in enumerate(is_prime):
            if flag == 1:
                primes.append(i + left)
            
            if len(primes) > 1:
                cur_diff = primes[-1] - primes[-2]
                if cur_diff == 1:
                    return [primes[-2], primes[-1]]
                elif cur_diff == 2:
                    return [primes[-2], primes[-1]]
                elif cur_diff < min_diff:
                    min_diff = cur_diff
                    result[0], result[1] = primes[-2], primes[-1]

        return result