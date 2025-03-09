class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        colors += colors[:k-1]
        num_groups = 0
        l = 0
        print(colors)
        for r in range(1, len(colors)):
            
            # if we find consecutive colors
            if colors[r - 1] == colors[r]:
                l = r
            
            # if window size is greater than k, shrink it
            if r - l + 1 > k:
                l += 1
            
            # correct size and valid window
            if r - l + 1 == k:
                num_groups += 1

        return num_groups