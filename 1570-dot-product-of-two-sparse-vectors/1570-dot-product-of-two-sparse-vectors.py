class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_nums = []
        for i, num in enumerate(nums):
            if num != 0:
                self.sparse_nums.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        i = 0
        j = 0
        product = 0
        while i < len(self.sparse_nums) and j < len(vec.sparse_nums):
            if self.sparse_nums[i][0] == vec.sparse_nums[j][0]:
                product += self.sparse_nums[i][1] * vec.sparse_nums[j][1]
                i += 1
                j += 1
            elif self.sparse_nums[i][0] > vec.sparse_nums[j][0]:
                j += 1
            else:
                i += 1
        return product

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)