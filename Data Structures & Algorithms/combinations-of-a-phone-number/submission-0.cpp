class Solution {
private:
    map<char, string> digit_to_char = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    void backtrack(string& digits, int i, string curr, vector<string>& ret) {
        if ( i == digits.size() ) {
            ret.push_back(curr);
            return;
        }
        for (char c : digit_to_char[digits[i]]) {
            backtrack(digits, i+1, curr+c, ret);
        }   
    }
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ret;
        if (digits=="") return ret;
        backtrack(digits, 0, "", ret);
        return ret;
    }
};
