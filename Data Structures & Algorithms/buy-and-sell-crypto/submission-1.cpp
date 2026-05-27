class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int curr_min = prices[0];
        int ret = 0;
        for (int i=1; i<prices.size(); i++) {
            if (prices[i]<=curr_min) {
                curr_min = prices[i];
            } else {
                ret = max(ret, prices[i]-curr_min);
            }
        }
        return ret;
    }
};
