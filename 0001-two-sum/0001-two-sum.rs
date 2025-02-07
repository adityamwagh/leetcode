use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new(); // Store number -> index
        
        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&j) = map.get(&complement) {
                return vec![j as i32, i as i32]; // Found the pair
            }
            map.insert(num, i); // Store current number's index
        }
        
        vec![] // Return empty if no solution found
    }
}
