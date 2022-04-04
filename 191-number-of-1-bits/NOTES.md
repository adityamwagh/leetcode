https://www.youtube.com/watch?v=5Km3utixwZs
​
There are two ways to solve this problem.
​
- Calculate the remainder when divided by 2, and keep adding it to get count. Then shift n to the right by one bit. This way we would have to iterate through all 32 bits of the number.
​
**Time Complexity: O(1), Space Complexity: O(1)**. Going through the number only 32 times, since there are only 32 bits. **Always O(32)**
​
- Compute the logical AND of `n` and `(n - 1)`. This way, the loop will as many times as there are number of ones in the binary number.
​
**Time Complexity: O(1), Space Complexity: O(1)**. Number of loop iterations = number of ones. **Worst case O(32) (all ones)**