use std::collections::HashMap;

impl Solution {
   /// Converts a Roman numeral string to its integer representation
   ///
   /// This function follows the standard Roman numeral conversion rules:
   /// - Numerals are typically added (XVI = 16)
   /// - When a smaller numeral precedes a larger one, it is subtracted (IV = 4)
   pub fn roman_to_int(s: String) -> i32 {
       // Initialize the result variable
       let mut num = 0;
       
       // Create a HashMap that maps each Roman numeral character to its integer value
       let cmaps = HashMap::from([
               ('I', 1),
               ('V', 5),
               ('X', 10),
               ('L', 50),
               ('C', 100),
               ('D', 500),
               ('M', 1000)
       ]);

       // Convert the input string to a vector of characters for easier indexing
       let chars: Vec<char> = s.chars().collect();

       // Iterate through each character in the string with its index
       for (i, &char) in chars.iter().enumerate() {
           // Check if the current character represents a value less than the next character
           // (if there is a next character)
           if i < chars.len() - 1 && cmaps[&chars[i]] < cmaps[&chars[i + 1]] {
               // If current value is less than next value, subtract it (like 'I' in "IV")
               num -= cmaps[&char];
           }
           else {
               // Otherwise, add the value to our running sum (regular case)
               num += cmaps[&char];
           }
       }
       // Return the final computed integer value
       num
   }
}