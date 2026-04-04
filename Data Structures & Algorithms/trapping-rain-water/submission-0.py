class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ret = 0

        left_max_height = [0]*n
        curr_max = 0
        for i in range(n):
            curr_max = max(curr_max, height[i])
            left_max_height[i] = curr_max

        right_max_height = [0]*n
        curr_max = 0
        for i in range(n-1, -1, -1):
            curr_max = max(curr_max, height[i])
            right_max_height[i] = curr_max

        ret = 0
        for i in range(1, n-1):
            min_max_height = min(left_max_height[i], right_max_height[i])
            if min_max_height > height[i]:
                ret += min_max_height - height[i]
        return ret
