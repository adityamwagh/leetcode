class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = deque(digits)
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + carry 
        
        
        return list(digits)
            if i == (len(digits) - 1):
                digits[i] += 1
            carry = digits[i] // 10
            digits[i] %= 10
            digits.appendleft(carry)
        if carry:
        # add leading digit

[
