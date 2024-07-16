class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hmap;
        for (auto i = 0; i < nums.size(); i++) {
            auto num = nums[i];
            auto residual = target - num;
            if (hmap.find(residual) != hmap.end()) {
                return {i, hmap[residual]};
            }
            hmap[num] = i;
        }
        return {};
    }
};