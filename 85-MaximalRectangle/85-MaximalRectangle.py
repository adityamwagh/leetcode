                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(row) - i))    
            return maxArea
        
        # find largest histogram array for each row
        maxArea = -float("inf")
        for row in cache:
            print(row, largestHistogramRectangleArea(row))
            maxArea = max(maxArea, largestHistogramRectangleArea(row))
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
