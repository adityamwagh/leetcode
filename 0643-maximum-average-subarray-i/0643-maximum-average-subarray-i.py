class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        windowSum = 0
        maxWindowAvg = float("-inf")
        start = 0

        for end in range(len(nums)):
            windowSum += nums[end]

            if end - start + 1 == k:
                currWindowAvg = windowSum / k
                maxWindowAvg = max(maxWindowAvg, currWindowAvg)
                windowSum -= nums[start]
                start += 1
        
        return maxWindowAvg