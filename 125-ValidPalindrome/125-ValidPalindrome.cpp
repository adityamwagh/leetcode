class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.size() - 1;

        while (l < r) {
            while (l < r && !isalnum(s[l])) l += 1;
            while (l < r && !isalnum(s[r])) r -= 1;
            if (tolower(s[l]) != tolower(s[r])) return false;
            r -= 1;
            l += 1;
        }
        return true;
    }
};
