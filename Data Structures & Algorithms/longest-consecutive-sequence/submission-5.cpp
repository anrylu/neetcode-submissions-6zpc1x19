class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if( nums.size() <= 1 ) return nums.size();
        int ret = 1;
        int len = 1;
        unordered_set seen(nums.begin(), nums.end());
        for (int num : seen) {
            if (seen.count(num-1)) continue;
            len = 1;
            while (seen.count(num+len)) len++;
            ret = max(ret, len);
        }
        return ret;
    }
};
