class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        for (const auto& s: strs) {
            vector<int> counter(26, 0);
            for (char c : s) {
                counter[c-'a'] += 1;
            }
            string key = to_string(counter[0]);
            for( int i=1; i<counter.size(); i++) {
                key += "," + to_string(counter[i]);
            }
            res[key].push_back(s);
        }
        vector<vector<string>> ret;
        for (const auto p : res) {
            ret.push_back(p.second);
        }
        return ret;
    }
};
