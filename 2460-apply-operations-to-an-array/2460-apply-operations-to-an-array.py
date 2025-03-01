class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []
        prev = nums[0]
        for i in range(1, n):
            print(f"i {i-1} nums[i].prev {prev} nums[i+1] {nums[i]} result {result}")
            if nums[i] == prev and prev != 0:
                result.append(prev * 2)
                prev = 0
            else:
                if prev != 0:
                    result.append(prev)
                prev = nums[i]
        result.append(prev)
        return result + [0] * (len(nums) - len(result))
