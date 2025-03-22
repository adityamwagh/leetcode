class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        t, b = 0, m - 1
        
        while t <= b and l <= r:
            # Top row
            for i in range(l, r + 1):
                result.append(matrix[t][i])
            t += 1
            if t > b:
                break
                
            # Right column
            for j in range(t, b + 1):
                result.append(matrix[j][r])
            r -= 1
            if l > r:
                break
                
            # Bottom row
            for k in range(r, l - 1, -1):
                result.append(matrix[b][k])
            b -= 1
            if t > b:
                break
                
            # Left column
            for o in range(b, t - 1, -1):
                result.append(matrix[o][l])
            l += 1

        return result