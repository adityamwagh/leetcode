class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h, v = 0, 0
        for move in moves:
            match move:
                case "R":
                    h += 1
                case "L":

                    h -= 1
                case "U":
                    v += 1
                case "D":
                    v -= 1
        
        return h == v == 0
            
"
