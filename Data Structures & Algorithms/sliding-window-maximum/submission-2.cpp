class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ret;
        deque<int> q;
        for (int r=0; r<nums.size(); r++) {
            while (!q.empty() and nums[q.back()]<nums[r]) {
                q.pop_back();
            }
            q.push_back(r);
            if (r>=k-1) {
                int l = r-k+1;
                while (q.front()<l) q.pop_front();
                ret.push_back(nums[q.front()]);
            }
        }
        return ret;
    }
};
