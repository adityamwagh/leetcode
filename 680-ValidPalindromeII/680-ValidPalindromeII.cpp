class Solution {
public:
    // Refactored isPalindrome to check in a range without creating substrings
    bool isPalindrome(const string& s, uint32_t l, uint32_t r) {
        while (l < r) {
            if (s.at(l) != s.at(r)) {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }

    bool validPalindrome(string s) {
        uint32_t l = 0, r = s.size() - 1;

        while (l < r) {
            if (s.at(l) != s.at(r)) {
                return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
            }
            l += 1;
            r -= 1;
        }

        return true;
    }
};