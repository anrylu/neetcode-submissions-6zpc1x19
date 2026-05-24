class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        
        def backtrack(i, j, result):
            if i == n and j == n:
                ret.append(''.join(result))
                return
            if i<n:
                result.append('(')
                backtrack(i+1, j, result)
                result.pop()
            if j<i:
                result.append(')')
                backtrack(i, j+1, result)
                result.pop()

        backtrack(0, 0, [])
        return ret