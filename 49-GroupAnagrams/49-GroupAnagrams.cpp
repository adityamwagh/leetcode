class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> amap;
        vector<vector<string>> anagram_list;

        for (const auto& str : strs) {

            vector<int> counts(26, 0);
            for (const auto& c : str) {
                counts[c - 'a']++;
            }
            string key = "";
            for (auto i {0}; i < 26; i++) {
                key += "#" + to_string(counts[i]);
            }
            amap[key].push_back(str); 
        }

        for (const auto& [word, anagrams] : amap) {
            anagram_list.push_back(anagrams);
        }
        return anagram_list;
    }
};