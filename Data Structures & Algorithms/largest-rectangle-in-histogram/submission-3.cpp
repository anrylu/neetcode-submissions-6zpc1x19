class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int i = 0;
        int ret = 0;
        for (i=0; i<heights.size(); i++) {
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
            int width = heights.size();
            if (!st.empty()) width -= st.top()+1;
            ret = max(ret, width*height);
        }
        return ret;
    }
};
