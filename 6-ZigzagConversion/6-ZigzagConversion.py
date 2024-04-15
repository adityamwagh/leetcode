        #     r -= 1
        #     c += 1
        #     r = 0
        #     print(f"r: {r}, c: {c}")
        #     print(zigzag)
    
        # return "".join(char for row in zigzag for char in row)
        if numRows == 1 or len(s) < numRows: return s
        r,c,t = 0,0,0
        ar  = []
        for _ in s:
            ar.append([r,c])
            if t == 1:
                r-=1
                c+=1
                if r == -1:
                    t = 0
                    r += 2
                    c-=1
            else: r+=1
            if r == numRows:
                t = 1
                r -= 2
                c += 1
        zigzag = [[""] * len(s) for _ in range(numRows)]
        for r, c in ar:
            zigzag[r][c] = s[i]
        i = 0
            i += 1
        
        return "".join(char for row in zigzag for char in row)
"
