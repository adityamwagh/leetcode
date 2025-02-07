use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<[i32; 26], Vec<String>> = HashMap::new();

        for s in strs {
            let mut count = [0; 26]; // Frequency array

            for c in s.chars() {
                count[(c as u8 - b'a') as usize] += 1;
            }

            map.entry(count).or_insert(Vec::new()).push(s);
        }

        map.into_values().collect()
    }
}
