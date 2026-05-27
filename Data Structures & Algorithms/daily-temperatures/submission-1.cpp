class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> st;
        vector<int> ret(n, 0);
        for (int i=0; i<n; i++) {
            while (!st.empty() && temperatures[st.top()]<temperatures[i]) {
                ret[st.top()] = i-st.top();
                st.pop();
            }
            st.push(i);
        }
        return ret;
    }
};
