class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        curr_min = prices[0]
        for p in prices:
            curr_min = min(curr_min, p)
            ret = max(ret, p-curr_min)
        return ret
        