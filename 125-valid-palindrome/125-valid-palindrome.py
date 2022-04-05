class Solution:
    
    def alphaNumeric(self, c: str) -> str:
        
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))
        
        
    def isPalindrome(self, s: str) -> bool:
        
        leftPtr, rightPtr = 0, len(s) - 1
        
        while leftPtr < rightPtr:
            
            while leftPtr < rightPtr and not self.alphaNumeric(s[leftPtr]):
                leftPtr += 1
            while rightPtr > leftPtr and not self.alphaNumeric(s[rightPtr]):
                rightPtr -= 1
            
            if s[leftPtr].lower() != s[rightPtr].lower():
                return False
            
            leftPtr, rightPtr = leftPtr + 1, rightPtr - 1
        
        return True
        
        