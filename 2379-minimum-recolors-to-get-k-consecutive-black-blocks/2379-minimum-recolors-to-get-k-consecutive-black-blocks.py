class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        min_rec, win_rec = len(blocks), 0
        s = 0
        for e in range(len(blocks)):
            if blocks[e] == "W":
                win_rec += 1
            if e - s + 1 == k:
                min_rec = min(min_rec, win_rec)
                if blocks[s] == "W":
                    win_rec -= 1
                s += 1
        
        return min_rec