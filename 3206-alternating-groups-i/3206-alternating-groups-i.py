class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        colors = colors + colors[:k]
        num_groups = 0
        
        def is_alternating(arr):
            n = len(arr)
            for i in range(1, n):
                if arr[i] == arr[i - 1]:  # Check if two consecutive elements are the same
                    return False
            return True

        for i in range(len(colors) - k):
            if is_alternating(colors[i:i + k]):
                num_groups += 1
        
        return num_groups
                    