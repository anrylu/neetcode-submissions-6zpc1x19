class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        vector<int> prefix_products(n+1, 1);
        for (i=0; i<n; i++) {
            prefix_products[i+1] = nums[i]*prefix_products[i];
        }
        vector<int> suffix_products(n+1, 1);
        for (i=n-1; i>=0; i--) {
            suffix_products[i] = nums[i]*suffix_products[i+1];
        }
        vector<int> ret(n);
        for (i=0; i<n; i++) {
            ret[i] = prefix_products[i]*suffix_products[i+1];
        }
        return ret;
    }
};
