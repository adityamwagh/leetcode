class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hmap = {}
        
        for num in nums:
            if num in hmap.keys():
                hmap[num] +=1
            else:
                hmap[num] = 1
        
        for key, val in hmap.items():
            if val > 1:
                return True
            
        return False