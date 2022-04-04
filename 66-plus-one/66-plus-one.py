class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        power = len(digits) - 1
        num = 0
        answer = []
        
        # compute value of n
        for digit in digits:
            num += (digit * (10 ** power))
            power -= 1
        # add one to num
        num = num + 1
        
        # convert n back to array
        while num > 0:
            digit = num % 10
            answer.append(digit)
            num = num // 10
            
        # reverse array to get the answer
        return answer[::-1]