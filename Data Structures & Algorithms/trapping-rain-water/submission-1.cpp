class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left_max_height(n+1, 0);
        vector<int> right_max_height(n+1, 0);
        int i = 0;
        for (i=0; i<n; i++)
            left_max_height[i+1] = max(left_max_height[i], height[i]);
        for (i=n-1; i>=0; i--)
            right_max_height[i] = max(right_max_height[i+1], height[i]);
        int ret = 0;
        for (i=0; i<n; i++) {
            int min_height = min(left_max_height[i], right_max_height[i+1]);
            if (height[i]<min_height)
                ret += min_height-height[i];
        }
        return ret;
    }
};
