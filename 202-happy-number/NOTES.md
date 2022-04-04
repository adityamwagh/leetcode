https://www.youtube.com/watch?v=ljz85bxOYJ0
​
It turns out that if the sum is not 1, it loops endlessly in a cycle (like a cycle in a graph or linkedlist). See above video for reference.
​
So, store each n in a set to account for uniqueness.Then compute the sum of it's digits' squares, and check if it's one. After some point, we will have reached all possible sums, and then if the sum is not one, we return False, else we return True.