class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i<n:
            x = nums[i]
            if (i+1) == x:
                i += 1
                continue
            if nums[x-1] == x:
                return x
            nums[i], nums[x-1] = nums[x-1], nums[i]
        return 0

