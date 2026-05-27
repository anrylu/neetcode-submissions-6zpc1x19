class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ret;
        priority_queue<pair<int, int>> q;
        for (int i=0; i<nums.size(); i++) {
            q.push({nums[i], i});
            if (i>=k-1) {
                while (q.top().second<i-k+1) {
                    q.pop();
                }
                ret.push_back(q.top().first);
            }
        }
        return ret;
    }
};
