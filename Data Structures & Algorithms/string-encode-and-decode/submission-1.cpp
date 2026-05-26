class Solution {
public:

    string encode(vector<string>& strs) {
        string ret;
        for (auto s : strs) {
            ret += to_string(s.size()) + "#" + s;
        }
        return ret;
    }

    vector<string> decode(string s) {
        vector<string> ret;
        int i = 0;
        while (i<s.size()) {
            int j = i;
            while (j<s.size() && s[j]!='#') j++;
            int len = stoi(s.substr(i, j-i));
            ret.push_back(s.substr(j+1, len));
            i = j+1+len;
        }
        return ret;
    }
};
