class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = []
        carry = 1
        for i in range(len(digits)-1, -1, -1):


            digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10

            print(digit, carry)
            result.append(digit)

        result.reverse()
        result = [1] + result if carry else result
        return result
