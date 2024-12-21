class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int cols = matrix[0].size();
        int rows = matrix.size();
        vector<vector<int>> matrix_transpose(cols, vector<int>(rows, 0));

        for (auto i = 0; i < rows; i++) {
            for (auto j = 0; j < cols; j++) {
                matrix_transpose.at(j).at(i) = matrix.at(i).at(j);
            }
        }
        return matrix_transpose;
    }
};