https://www.youtube.com/watch?v=RyBM56RIWrM
​
* **Approach 1: O(nlogn)**: Get number of ones by computing **AND** operation of `n` and `n-1`, until `n > 0` After that, for each `i` from 0 to n (including n), compute the number of ones, and add them to output array.
​
* **Approach 2: O(n)**: Write the bit representations of numbers from 0 to 8, and then you will see a pattern - a recurrence, `a[i] = 1 + a[i - offset]`. Offset keeps increasing as a  power of 2. (See the code for a cleareer picture)
​