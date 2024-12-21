class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (auto r = 0; r < matrix.size(); r++) {
            for (auto c = 0; c <=r; c++) {
                std::swap(matrix.at(r).at(c), matrix.at(c).at(r)); 
            }
        }
        
        for (auto i = 0; i < matrix.size(); i++) {
            std::reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};