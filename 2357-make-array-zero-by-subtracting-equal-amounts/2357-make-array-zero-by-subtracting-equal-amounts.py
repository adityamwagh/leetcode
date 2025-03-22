class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        n_operations = 0
        
        while any(nums): 
            m = min(x for x in nums if x > 0)  # Find min of non-zero elements
            if m == 0:  # Skip if min is already 0
                break
                
            for i in range(len(nums)):
                if nums[i] > 0:  # Only subtract from non-zero elements
                    nums[i] -= m
            
            n_operations += 1
        
        return n_operations