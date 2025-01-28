class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<vector<int>> triplets;
        for (int i = 0; i < nums.size(); ++i) {
            int l = i + 1, r = nums.size() - 1;
            while (l < nums.size() && l < r) {
                long int total = nums.at(i) + nums.at(l) + nums.at(r);
                if (total == 0) {
                    triplets.insert({nums.at(i), nums.at(l), nums.at(r)});
                    l++;
                    r--;
                }
                else if (total < 0) {
                    l++;
                }
                else {
                    r--;
                }
            }
        }
        return vector<vector<int>>(triplets.begin(), triplets.end());
    }
};
