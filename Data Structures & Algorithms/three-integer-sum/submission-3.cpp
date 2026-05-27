class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size()-2; i++) {
            int j = i+1;
            int k = nums.size()-1;
            if (i>0 && nums[i] == nums[i-1]) continue;
            while (j<k) {
                if (j>i+1 && nums[j] == nums[j-1]) {
                    j++;
                    continue;
                }
                if (k<nums.size()-1 && nums[k] == nums[k+1]) {
                    k--;
                    continue;
                }
                int sum = nums[i] + nums[j] + nums[k];
                if (sum>0) k--;
                else if (sum<0) j++;
                else {
                    ret.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                }
            } 
        }
        return ret;
    }
};
