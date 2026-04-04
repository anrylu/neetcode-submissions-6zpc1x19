class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        nums.sort()
        dp = [1]*n

        for i in range(1, n):
            for j in range(i):
                if nums[i] == (nums[j]+1):
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)