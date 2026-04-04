class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        nums.sort()

        ret = 1
        visited = {}
        for i in range(n):
            target = nums[i] - 1
            if nums[i] not in visited:
                visited[nums[i]] = 1
            if target in visited:
                visited[nums[i]] = max(visited[nums[i]], visited[target] + 1)
            ret = max(ret, visited[nums[i]])
        return ret