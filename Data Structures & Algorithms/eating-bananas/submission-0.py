class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_good(rate):
            nonlocal h
            t = 0
            for p in piles:
                t += (p+rate-1)//rate
            return t<=h
        
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2
            if is_good(mid):
                high = mid
            else:
                low = mid + 1
        return low
