                    continue
                if e == ".":
                e = board[r][c]
            for c in range(9):
        for r in range(9):

        sqrs = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                if (e in rows[r] or e in cols[c] or e in sqrs[(r // 3, c // 3)]):
                    return False
[
