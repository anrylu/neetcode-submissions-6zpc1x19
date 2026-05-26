class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if( nums.size() <= 1 ) return nums.size();
        sort(nums.begin(), nums.end());

        int prev = nums[0];
        int ret = 1;
        int count = 1;
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] == prev) {
                continue;
            }
            if (nums[i] == (prev+1)) {
                count += 1;
            } else {
                count = 1;
            }
            ret = max(ret, count);
            prev = nums[i];
        }
        return ret;
    }
};
