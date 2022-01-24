class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        // store length of nums array
        const int len = nums.size();
        
        // intialize vectors to store count of element 
        // and elements that aren't present
        vector<int> count(len);
        vector<int> not_present;
        
        // iterate through the array and count number of all elements 
        for(auto num: nums){
            count[num - 1] += 1;
        }
        
        // see which elements are not present and add them to not_present
        for (int i = 0; i < count.size(); ++i){
            if (count[i] == 0) not_present.push_back(i + 1);
        }
        
        return not_present;
    }
};