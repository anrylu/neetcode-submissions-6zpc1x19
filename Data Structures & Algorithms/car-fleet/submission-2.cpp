class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int i = 0;

        // sort reversely by position & speed
        vector<pair<int, int>> pairs;
        for (i=0; i<position.size(); i++) {
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.rbegin(), pairs.rend());

        // calc arrival time one by one
        double curr = 0;
        int ret = 0;
        for (pair p : pairs) {
            double arrival_time = (double)(target-p.first)/p.second;
            if (arrival_time>curr) {
                ret += 1;
                curr = arrival_time;
            }
        }
        return ret;
    }
};
