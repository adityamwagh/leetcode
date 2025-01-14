class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()) return false;

        vector<int> counts(26, 0);
        for (auto i = 0; i < s.size(); ++i) {
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }

        return std::all_of(counts.begin(), counts.end(), [](int val){ return val == 0; });
    }
};
