use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_set: HashSet<char> = HashSet::new();
        let chars: Vec<char> = s.chars().collect();
        let mut start = 0;
        let mut max_length = 0;
        
        for end in 0..chars.len() {
            let current_char = chars[end];
            
            // While we have a duplicate, remove characters from start
            while char_set.contains(&current_char) {
                char_set.remove(&chars[start]);
                start += 1;
            }
            
            char_set.insert(current_char);
            max_length = std::cmp::max(max_length, end - start + 1);
        }
        
        max_length as i32
    }
}