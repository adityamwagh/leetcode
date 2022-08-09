class Solution {
public:
    bool isAnagram(string s, string t) {
        
        // unequal strings
        if (s.size() != t.size()) {
            return false;
        }
        
        // store the element and count in string
        map<char, int> a;
        map<char, int> b;
        
        // populate corresponding maps
        for (auto& i: s) {
            if (a.find(i) == a.end()) {
                a.insert(pair<char, int>(i, 1));
            }
            else a[i]++;
        }
        
        for (auto& j: t) {
            if (b.find(j) == b.end()) {
                b.insert(pair<char, int>(j, 1));
            }
            else b[j]++;
        }
        
        if (a == b) {
            return true;
        }
        
        return false;
    }
};