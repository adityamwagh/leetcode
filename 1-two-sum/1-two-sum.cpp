class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map <int, int> m;
        vector <int> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (m.find(complement) != m.end()) {
                result.emplace_back(m[complement]);
                result.emplace_back(i);
            }
            else {
                m.insert({nums[i], i});
            }
        }
        return result;
    }
};