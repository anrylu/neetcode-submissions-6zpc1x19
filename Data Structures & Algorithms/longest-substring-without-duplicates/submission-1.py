class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = {}
        ret = 0
        for right, c in enumerate(s):
            if c in visited:
                left = max(left, visited[c] + 1)
            visited[c] = right
            ret = max(ret, right-left+1)
        return ret

