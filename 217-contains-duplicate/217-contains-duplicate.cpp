class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        // check for empty input
        if (nums.size() == 0) return false;

        // make a dict to store values
        map<int, int> dups;

        // iterate through vector
        for (auto num : nums) {

            // if element is not in dict, add it.
            if (dups.find(num) == dups.end()) dups.insert(pair<int, int>(num, 1));

            // else, increase the count of element by 1
            else dups[num] += 1;

            // return true if element is duplicate
            if (dups[num] > 1) return true;
        }
        return false;
    }
};