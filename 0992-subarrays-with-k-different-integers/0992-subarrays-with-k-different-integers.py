class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atleast_k_integers(k):
            ints = defaultdict(int)
            l = 0
            subarrs = 0

            for r in range(len(nums)):

                ints[nums[r]] += 1

                while len(ints) >= k:
                    subarrs += (len(nums) - r)
                    
                    ints[nums[l]] -= 1
                    if ints[nums[l]] == 0:
                        ints.pop(nums[l])
                    l += 1
            return subarrs

        return atleast_k_integers(k) - atleast_k_integers(k+1)

