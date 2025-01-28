class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        n = len(nums)
        for i in range(n):
            l, r = i + 1, n - 1
            while (l < n and l < r):
                target = nums[i] + nums[l] + nums[r]
                if (nums[i] + nums[l] + nums[r]) == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in triplets]