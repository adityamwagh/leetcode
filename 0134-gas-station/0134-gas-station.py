class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        if sum(diff)<0:
            return -1
        minidx = 0
        runval = 0
        for i in range(n):
            runval+=diff[i]
            if runval<0:
                runval = 0
                minidx = i+1
        if minidx==n:
            return -1
        return minidx
