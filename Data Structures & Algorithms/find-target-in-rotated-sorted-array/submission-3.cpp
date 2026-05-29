class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int low = 0;
        int high = n-1;
        int pivot = 0;

        while (low<high) {
            int mid = (low+high)/2;
            if (nums[mid]>nums[n-1]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        pivot = low;

        low = 0;
        high = n-1;
        while (low<=high) {
            int mid = (low+high)/2;
            int pos = (mid+pivot)%n;
            if (nums[pos]>target) {
                high = mid - 1;
            } else if (nums[pos]<target) {
                low = mid + 1;
            } else {
                return pos;
            }
        }
        return -1;
    }
};
