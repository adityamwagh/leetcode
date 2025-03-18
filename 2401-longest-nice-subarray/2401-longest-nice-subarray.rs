impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 1 {
            return 1;
        }
        
        let mut left = 0;
        let mut used_bits = 0; // Track which bits are used in our current window
        let mut max_length = 1; // Minimum nice subarray length is 1
        
        for right in 0..n {
            // While the current number has bits that conflict with our window
            while (used_bits & nums[right]) != 0 {
                // Remove the leftmost number's bits
                used_bits ^= nums[left];
                left += 1;
            }
            
            // Add current number's bits to our used_bits
            used_bits |= nums[right];
            
            // Update max length
            max_length = max_length.max(right - left + 1);
        }
        
        max_length as i32
    }
}