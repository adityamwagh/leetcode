class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        # min swaps = min num zeros in window of all ones
        min_zeros, win_zeros = len(data), 0
        ones = sum(data)
        if ones == 0: return 0
        s = 0

        for e in range(len(data)):
            if data[e] == 0:
                win_zeros += 1
            if e - s + 1 == ones:
                min_zeros = min(min_zeros, win_zeros)
                if data[s] == 0:
                    win_zeros -= 1
                s += 1
                
        return min_zeros
