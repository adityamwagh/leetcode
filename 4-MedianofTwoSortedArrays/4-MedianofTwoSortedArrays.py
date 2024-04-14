class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def median(array):
            n = len(array)
            if n % 2 == 0:
                return (array[n // 2 - 1] + array[n // 2]) / 2
            else:
                return array[n // 2]
        return median(sorted(nums1 + nums2))
[
