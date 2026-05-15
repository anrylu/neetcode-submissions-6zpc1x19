class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []

        def backtracking(i, v):
            if i == n:
                ret.append(v[:])
                return
            v.append(nums[i])
            backtracking(i+1, v)
            v.pop()
            backtracking(i+1, v)
        backtracking(0, [])
        return ret