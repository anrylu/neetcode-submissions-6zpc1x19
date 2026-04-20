class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ret = 0
        for right in range(n):
            while stack and heights[stack[-1]]>=heights[right]:
                height = heights[stack[-1]]
                left = stack[-1]
                stack.pop()
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                ret = max(ret, height*(right-left))
            stack.append(right)
        while stack:
            height = heights[stack[-1]]
            left = stack[-1]
            stack.pop()
            if stack:
                left = stack[-1] + 1
            else:
                left = 0
            ret = max(ret, height*(n-left))
        return ret