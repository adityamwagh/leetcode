# class Solution:
#     def closestPrimes(self, left: int, right: int) -> List[int]:
        
#         is_prime = [1] * (right - left + 1)
#         primes = []
#         result = [-1, -1]
#         min_diff = float("inf")

#         # case when range starts from 1
#         if left == 1:
#             if right <= 2:
#                 return result
#             if right > 2:
#                 return [2, 3]
        
#         # find all primes in range
#         for k in range(left, right + 1):
#             for i in range(2, math.ceil(math.sqrt(k)) + 1):
#                 if k % i == 0:
#                     is_prime[k - left] = 0
#                     break
        
#         # collect all primes
#         for i, flag in enumerate(is_prime):
#             if flag == 1:
#                 primes.append(i + left)
            
#             if len(primes) > 1:
#                 cur_diff = primes[-1] - primes[-2]
#                 if cur_diff == 1:
#                     return [primes[-2], primes[-1]]
#                 elif cur_diff == 2:
#                     return [primes[-2], primes[-1]]
#                 elif cur_diff < min_diff:
#                     min_diff = cur_diff
#                     result[0], result[1] = primes[-2], primes[-1]

#         return result
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Use Sieve of Eratosthenes for finding primes
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        
        # Mark non-primes using Sieve approach
        for i in range(2, int(right**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples as non-prime
                for j in range(i*i, right + 1, i):
                    is_prime[j] = False
        
        # Collect primes only in the specified range
        primes = [i for i in range(max(2, left), right + 1) if is_prime[i]]
        
        # Early exit cases
        if len(primes) < 2:
            return [-1, -1]
        
        # Find closest pair in a single pass
        min_diff = float("inf")
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i-1], primes[i]]
                
                # Early return for minimum possible difference (2)
                if min_diff == 2:
                    return result
        
        return result