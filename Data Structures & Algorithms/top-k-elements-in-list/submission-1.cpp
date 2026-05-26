class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        for (auto num : nums) {
            counter[num] += 1;
        }

        vector<vector<int>> buckets(nums.size()+1);
        for (auto p : counter) {
            buckets[p.second].push_back(p.first);
        }

        vector<int> ret;
        for (int i=nums.size(); i>0; i--) {
            for (int v : buckets[i]) {
                ret.push_back(v);
                if( ret.size() >= k ) {
                    return ret;
                }
            }
        }
        return ret;
    }
};
