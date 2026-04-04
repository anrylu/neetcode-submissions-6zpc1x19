class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            target = -nums[i]
            left = i+1
            right = n-1
            while left<right:
                v = nums[left] + nums[right]
                if v == target:
                    ret.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif v < target:
                    left += 1
                else:
                    right -= 1
        return [[i, j, k] for i, j, k in ret]