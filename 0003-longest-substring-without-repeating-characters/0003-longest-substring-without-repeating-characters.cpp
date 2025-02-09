class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        vector<bool> seen(256, false);
        int start = 0;
        int longest = 0;

        for (int end = 0; end < s.size(); end++) {

            while (seen[s[end]]) {
                seen[s[start]] = false;
                start++;
            }

            // mark current as seen
            seen[s[end]] = 1;
            longest = max(longest, end - start + 1);
        }
        return longest;
    }
};