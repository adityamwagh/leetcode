class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:

        result = defaultdict(int)

        for num, val in nums1:
            result[num] += val
        
        for num, val in nums2:
            result[num] += val
        
        return list(sorted(result.items()))