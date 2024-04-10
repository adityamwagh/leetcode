        
        # find odd & even indices
        even, odd = [], []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        # sort elements
        even.sort()
        odd.sort(reverse=True)

        # add elements of num to ans
        for i in range(n):
                ans.append(even[j])
                ans.append(odd[k])
        n, ans = len(nums), []
            if i % 2 == 0:
        j, k = 0, 0
                j += 1
            else:
                k += 1
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
[
