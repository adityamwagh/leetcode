// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        uint64_t left { 1 }, right { static_cast<uint64_t>(n) }, mid;
        while (left < right) {
            mid = left + (right - left) / 2;
                left = mid + 1;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
            }
        }
        return left;
    }
};
5
