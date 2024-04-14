class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mmap = Counter(moves)
        return mmap["R"] == mmap["L"] and mmap["U"] == mmap["D"]
"
