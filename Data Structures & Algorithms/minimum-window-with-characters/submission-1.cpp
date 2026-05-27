class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length()<t.length()) return "";

        int i = 0;
        unordered_map<char, int> counter_t;
        for (i=0; i<t.length(); i++) {
            counter_t[t[i]]++;
        }
        int required = counter_t.size();

        int have = 0;
        unordered_map<char, int> counter_s;
        string ret = "";
        i = 0;
        for (int j=0; j<s.length(); j++) {
            counter_s[s[j]]++;
            if (counter_s[s[j]] == counter_t[s[j]]) {
                have++;
            }
            while (have == required) {
                if (ret.length()==0 || ret.length()>j-i+1)
                    ret = s.substr(i, j-i+1);
                if (counter_s[s[i]] == counter_t[s[i]]) {
                    have--;
                }
                counter_s[s[i]]--;
                i++;
            }
        }
        return ret;
    }
};
