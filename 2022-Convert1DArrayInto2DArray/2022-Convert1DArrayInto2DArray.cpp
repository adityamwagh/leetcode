class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if (m * n != original.size()) {
            return {};
        }
        vector<vector<int>> output {};
        for (auto i = 0; i < m * n; i += n) {
            vector<int> current_row(original.begin() + i, original.begin() + i + n);
            output.push_back(current_row);
        }

        return output;
    }
};