class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        m, n = len(nums1), len(nums2)
        target = (m+n)//2
        is_even = (m+n)%2 == 0

        median = prev_median = 0
        while (i+j)<=target:
            prev_median = median
            if i<m and j<n:
                if nums1[i]<nums2[j]:
                    median = nums1[i]
                    i += 1
                else:
                    median = nums2[j]
                    j += 1
            elif i<m:
                median = nums1[i]
                i += 1
            else:
                median = nums2[j]
                j += 1
        if is_even:
            median = (median + prev_median)/2
        return median