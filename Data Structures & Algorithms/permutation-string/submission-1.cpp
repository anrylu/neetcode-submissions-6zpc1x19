class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int i = 0, j = 0;
        if (s1.length()>s2.length()) return false;

        vector<int> counter_s1(26, 0);
        for (i=0; i<s1.length(); i++) counter_s1[s1[i]-'a']++;
        vector<int> counter_s2(26, 0);
        for (i=0; i<s1.length(); i++) counter_s2[s2[i]-'a']++;

        int diff_count = 0;
        for (i=0; i<26; i++) {
            if (counter_s1[i] != counter_s2[i]) {
                diff_count++;
            }
        }
        if (diff_count == 0) return true;

        for (j=s1.length(); j<s2.length(); j++) {
            int add_char = s2[j]-'a';
            int remove_char = s2[j-s1.length()]-'a';
            if (counter_s1[add_char] == counter_s2[add_char]) diff_count++;
            counter_s2[add_char]++;
            if (counter_s1[add_char] == counter_s2[add_char]) diff_count--;
            if (counter_s1[remove_char] == counter_s2[remove_char]) diff_count++;
            counter_s2[remove_char]--;
            if (counter_s1[remove_char] == counter_s2[remove_char]) diff_count--;
            if (diff_count == 0) return true;
            cout << "j: " << j << ", diff_count: " << diff_count << endl;
        }
        return false;
    }
};
