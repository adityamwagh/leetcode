class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        maxSum = -1
        def sum_of_digits(x):
            x = str(x)
            return sum(int(d) for d in x)

        sums = list(map(sum_of_digits, nums))
        cmap = {nums[i] : sums[i] for i in range(len(nums))}
        smap = defaultdict(SortedList)
        for _num, _sum in cmap.items():
            smap[_sum].add(_num)
        
        for nums in smap.values():
            if len(nums) > 1:
                maxSum = max(maxSum, nums[-1] + nums[-2])
        return maxSum