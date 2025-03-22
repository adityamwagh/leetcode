class MovingAverage:

    def __init__(self, size: int):
        
        self.data = deque()
        self.size = size
        self.window_sum = 0

    def next(self, val: int) -> float:
        
        self.data.append(val)
        self.window_sum += val
        
        if len(self.data) > self.size:
            self.window_sum -= self.data.popleft()
        
        return self.window_sum / len(self.data)



    

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)