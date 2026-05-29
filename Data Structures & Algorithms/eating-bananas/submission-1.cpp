class Solution {
    int required_h(vector<int>& piles, int k) {
        int ret = 0;
        for (int p : piles) {
            ret += (p+k-1)/k;
        }
        return ret;
    }
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());

        while(low<high) {
            int k = (low+high)/2;
            int x = required_h(piles, k);
            if (x<=h) {
                high = k;
            } else {
                low = k+1;
            }
        }
        return low;
    }
};
