class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int n = heights.size();
        int ret = 0;
        for (int i=0; i<n; i++) {
            while (!st.empty() && heights[st.top()]>=heights[i]) {
                int height = heights[st.top()]; st.pop();
                int width = i;
                if (!st.empty()) width -= st.top()+1;
                ret = max(ret, width*height);
            }
            st.push(i);
        }
        while (!st.empty()) {
            int height = heights[st.top()]; st.pop();
            int width = n;
            if (!st.empty()) width -= st.top()+1;
            ret = max(ret, width*height);
        }
        return ret;
    }
};
