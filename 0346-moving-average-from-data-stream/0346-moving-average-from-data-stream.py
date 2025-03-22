class MovingAverage:

    def __init__(self, size: int):
        
        self.data = []
        self.size = size
        self.curr_size = 0

    def next(self, val: int) -> float:
        
        self.data.append(val)
        self.curr_size += 1
        total = 0
        average = 0
        if self.curr_size < self.size:
            for i in range(1, self.curr_size + 1):
                total += self.data[-i]
            average = total / self.curr_size
        else:
            for i in range(1, self.size + 1):
                total += self.data[-i]
            average = total / self.size
        return average

    

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)