class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size()-1;
        int ret = 0;
        while (left<right) {
            ret = max(ret, (right-left)*min(heights[left], heights[right]));
            if (heights[left]<heights[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return ret;
    }
};
