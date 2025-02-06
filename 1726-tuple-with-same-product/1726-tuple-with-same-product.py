class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # store products and their counts
        counts = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                counts[product] +=1 

        # for each count, the number of pairs is current count + previous pairs for count - 1, which is sum of all numbers from 0 to count - 1
        return 8 * sum([c * (c - 1) // 2 for c in counts.values()])