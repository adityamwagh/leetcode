class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1); // Result array initialized to 1

        // Compute prefix product for each element
        int prefix = 1;
        for (int i = 0; i < n; ++i) {
            result[i] = prefix;   // Store the prefix product
            prefix *= nums[i];    // Update prefix product
        }

        // Compute suffix product and multiply with the prefix product
        int suffix = 1;
        for (int i = n - 1; i >= 0; --i) {
            result[i] *= suffix;  // Multiply with the suffix product
            suffix *= nums[i];    // Update suffix product
        }

        return result;
    }
};
