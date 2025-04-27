class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        
        int n_subarrays {0};
        for (size_t i {0}; i < nums.size() - 2; i++) {
            if (2 * (nums[i] + nums[i+2]) == nums[i+1]) {
                n_subarrays++;
            }
        }
        return n_subarrays;
    }
};