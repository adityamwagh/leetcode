class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        total = 0
        
        # For each index i, count how many previous values of j-nums[j] match i-nums[i]
        for i, num in enumerate(nums):
            diff = i - num
            total += i - seen[diff]  # i is total elements seen so far, seen[diff] is valid pairs
            seen[diff] += 1
            
        return total