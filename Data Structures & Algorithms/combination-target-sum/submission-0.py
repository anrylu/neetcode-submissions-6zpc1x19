class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        n = len(nums)
        
        def backtrack(start, curr, result):
            if curr == target:
                ret.append(result[:])
                return
            if curr > target:
                return
            for i in range(start, n):
                result.append(nums[i])
                backtrack(i, curr+nums[i], result)
                result.pop()
        
        backtrack(0, 0, [])
        return ret