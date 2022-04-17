class Solution:
    
    def binarySearch(self, nums, target):
        
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1
                
            
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         # O(n^2)
#         m, n = len(matrix), len(matrix[0])
        
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == target:
#                     return True
                
#         return False
        
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            isPresent = self.binarySearch(matrix[i], target)
            if isPresent:
                return True
            
        return False