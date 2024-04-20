            if i not in range(r[0],r[1]):
                c[t] += 1 if l == 0 else -1
            i += steps[k][0]
            j += steps[k][1]
            res.append(matrix[i][j])
                i -= steps[k][0]
                t = abs(t-1)
                k += 1
                if k > 3:
                    k = 0
                j += steps[k][1]
            elif j not in range(c[0],c[1]):
                r[l] += 1 if l == 0 else -1
                j -= steps[k][1]
[
