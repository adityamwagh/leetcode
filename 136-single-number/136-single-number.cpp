class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        // variable to store answer
        int answer = 0;
        
        // loop and compute xor of all elements
        for (auto num: nums) answer = answer ^ num;
        
        // return answer
        return answer;
    }
};