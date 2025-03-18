struct SparseVector {
	sparse_nums: Vec<(i32, i32)>,
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SparseVector {
    fn new(nums: Vec<i32>) -> Self {
        
        let mut sparse_nums =  Vec::new();
        for (i, &num) in nums.iter().enumerate() {
            if num != 0 {
                sparse_nums.push((i as i32, num));
            }
        }
        SparseVector { sparse_nums }
    }
	
    // Return the dotProduct of two sparse vectors
    fn dot_product(&self, vec: SparseVector) -> i32 {
        
        // Early termination check
        if self.sparse_nums.is_empty() || vec.sparse_nums.is_empty() {
            return 0;
        }
        let mut i = 0;
        let mut j = 0;
        let mut product = 0;

        while i < self.sparse_nums.len() && j < vec.sparse_nums.len() {
            if self.sparse_nums[i].0 == vec.sparse_nums[j].0 {
                product += self.sparse_nums[i].1 * vec.sparse_nums[j].1;
                i += 1;
                j += 1;
            }
            else if self.sparse_nums[i].0 > vec.sparse_nums[j].0 {
                j += 1;
            }
            else {
                i += 1;
            }
        }
        product
    }
}

/**
 * Your SparseVector object will be instantiated and called as such:
 * let v1 = SparseVector::new(nums1);
 * let v2 = SparseVector::new(nums2);
 * let ans = v1.dot_product(v2);
 */
