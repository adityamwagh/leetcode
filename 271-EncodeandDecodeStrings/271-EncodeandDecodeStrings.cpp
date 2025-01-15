class Codec {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string enc = "";
        for (const auto& str : strs) {
            enc += (to_string(str.size()) + "#" + str);
        }
        return enc;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> strs;
        int i = 0;

        while (i < s.size()) {
            // Find the position of the `#` separator
            size_t pos = s.find('#', i);
            if (pos == string::npos) {
                break; // No more `#`, exit the loop
            }

            // Parse the length of the next string
            int len =
                stoi(s.substr(i, pos - i)); // Extract the number before `#`
            i = pos + 1;                    // Move past the `#`

            // Extract the substring of the given length
            strs.emplace_back(s.substr(i, len));
            i += len; // Move to the next encoded segment
        }

        return strs;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));