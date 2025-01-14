class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> imap;
        for (auto i {0}; i < nums.size(); i++) {
            int complement = target - nums.at(i);
            if (imap.count(complement) > 0) {
                return {
                    min(i, imap.at(complement)),
                    max(i, imap.at(complement))
                };
            }
            imap[nums.at(i)] = i;
        }
        return {};
    }
};
