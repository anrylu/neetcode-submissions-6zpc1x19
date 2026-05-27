class Solution {
public:
    int characterReplacement(string s, int k) {
        int n = s.length();
        int i = 0;
        int ret = 0;
        int max_freq = 0;
        unordered_map<char, int> counter;
        for (int j=0; j<n; j++) {
            counter[s[j]]++;
            max_freq = max(max_freq, counter[s[j]]);
            while ((j-i+1-max_freq)>k) {
                counter[s[i]]--;
                i += 1;
            }
            ret = max(ret, j-i+1);
        }
        return ret;
    }
};
