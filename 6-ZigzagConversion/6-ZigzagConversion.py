        #     r -= 1
        #     c += 1
        #     r = 0
        #     print(f"r: {r}, c: {c}")
        #     print(zigzag)
    
        # return "".join(char for row in zigzag for char in row)
        if numRows == 1 or len(s) < numRows: return s
        r,c,t = 0,0,0
        ar  = [[] for _ in range(numRows)]
        for i in s:
            ar[r].append(i)
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
        return ''.join(char for row in ar for char in row)
        #     print(f"r: {r}, c: {c}")
"
