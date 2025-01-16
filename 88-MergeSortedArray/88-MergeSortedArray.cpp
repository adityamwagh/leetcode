class Solution {
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        std::vector<int> temp(m + n);
        std::merge(nums1.begin(), nums1.begin() + m, nums2.begin(), nums2.begin() + n, temp.begin());
        std::copy(temp.begin(), temp.end(), nums1.begin());
    }
};
