class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        def backtrack(result, visited):
            if len(visited) == len(nums):
                ret.append(result[:])
            for i in range(n):
                if nums[i] in visited: continue
                result.append(nums[i])
                visited.add(nums[i])
                backtrack(result, visited)
                visited.remove(nums[i])
                result.pop()
        
        backtrack([], set())
        return ret