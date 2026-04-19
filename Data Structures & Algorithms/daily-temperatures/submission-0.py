class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0]*n
        stack = []
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                ret[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        return ret