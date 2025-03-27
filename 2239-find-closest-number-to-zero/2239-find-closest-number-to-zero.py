class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        # Initialize variables to track the closest number
        closest = nums[0]
        min_distance = abs(nums[0])
        
        # Iterate through the array
        for num in nums:
            current_distance = abs(num)
            
            # Update closest number if:
            # 1. Current number has smaller absolute distance, OR
            # 2. Current number has equal distance but is larger
            if current_distance < min_distance or \
            (current_distance == min_distance and num > closest):
                closest = num
                min_distance = current_distance
        
        return closest