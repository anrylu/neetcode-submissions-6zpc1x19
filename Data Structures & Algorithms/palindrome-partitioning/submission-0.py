class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ret = []

        def is_palindromic(s):
            left, right = 0, len(s)-1
            while left<right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        
        def backtrack(result, i):
            if i == n:
                ret.append(result[:])
                return
            for j in range(i, n):
                target = s[i:j+1]
                if not is_palindromic(target): continue
                result.append(target)
                backtrack(result, j+1)
                result.pop()
        
        backtrack([], 0)
        return ret
            