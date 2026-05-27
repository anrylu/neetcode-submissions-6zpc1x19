class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length();
        while (left<right) {
            if (!isalnum(s[left])) {
                left += 1;
                continue;
            }
            if (!isalnum(s[right])) {
                right -= 1;
                continue;
            }
            if (tolower(s[left]) != tolower(s[right]))
                return false;
            left += 1;
            right -= 1;
        }
        return true;
    }
};
