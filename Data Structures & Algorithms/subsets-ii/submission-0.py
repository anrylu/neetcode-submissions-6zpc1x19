class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        counter_keys = list(sorted(counter.keys()))
        n = len(counter_keys)
        ret = []

        def backtrack(i, result):
            if i == n:
                ret.append(result[:])
                return
            backtrack(i+1, result)
            key = counter_keys[i]
            for j in range(counter[key]):
                backtrack(i+1, result + [key]*(j+1))
        backtrack(0, [])

        return ret