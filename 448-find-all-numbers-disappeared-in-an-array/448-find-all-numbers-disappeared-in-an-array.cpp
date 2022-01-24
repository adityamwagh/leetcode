class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        const int len = nums.size();
            
        vector<int> count(len);
        vector<int> not_present;
        
        for(auto num: nums){
            count[num - 1] += 1;
        }
        
        for (int i = 0; i < count.size(); ++i){
            if (count[i] == 0) not_present.push_back(i + 1);
        }
        
        return not_present;
    }
};