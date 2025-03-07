class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        is_prime = [True] * (right + 1)
        is_prime[0]=is_prime[1]=False
        result = [-1, -1]
        min_diff = float("inf")
        primes = []
        last = None

        # case when range starts from 1
        if left == 1:
            if right <= 2:
                return result
            if right > 2:
                return [2, 3]
        
        # find all primes in range
        for i in range(2, int(sqrt(right))+1):
            if is_prime[i]:
                for j in range(2*i, right+1, i):
                    is_prime[j]=False
        
        
        #collect all primes
        for i in range(left, right+1):
            if is_prime[i]:
                if last and i-last<min_diff:
                    min_diff = i-last
                    result = [last, i]
                last = i

        return result
