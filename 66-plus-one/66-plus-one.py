class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
#         power = len(digits) - 1
#         num = 0
#         answer = []
        
#         # compute value of n
#         for digit in digits:
#             num += (digit * (10 ** power))
#             power -= 1
#         # add one to num
#         num = num + 1
        
#         # convert n back to array
#         while num > 0:
#             digit = num % 10
#             answer.append(digit)
#             num = num // 10
            
#         # reverse array to get the answer
#         return answer[::-1]
        
        digits = digits[::-1]
        
        carry, i = 1, 0
        n = len(digits)
        while carry:
            if i < n:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(carry)
                carry = 0
            i += 1
            
        return digits[::-1]