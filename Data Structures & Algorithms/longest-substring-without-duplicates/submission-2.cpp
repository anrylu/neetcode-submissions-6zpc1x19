class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> char2pos;
        int i = 0;
        int ret = 0;
        for (int j=0; j<s.length(); j++) {
            if (char2pos.find(s[j]) != char2pos.end() && char2pos[s[j]]>=i) {
                i = char2pos[s[j]] + 1;
            }
            char2pos[s[j]] = j;
            ret = max(ret, j-i+1);
        }
        return ret;
    }
};
