class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        counter_keys = list(counter.keys())
        counter_keys.sort()
        n = len(counter_keys)
        ret = []

        def backtrack(i, curr, result):
            if curr == target:
                ret.append(result[:])
                return
            if i == n:
                return
            backtrack(i+1, curr, result)
            candidate = counter_keys[i]
            for j in range(counter[candidate]):
                curr += candidate
                if curr > target: break
                backtrack(i+1, curr, result+[candidate]*(j+1))
            
        backtrack(0, 0, [])
        return ret