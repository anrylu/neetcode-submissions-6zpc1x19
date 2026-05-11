class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-s for s in stones]
        heapq.heapify(q)
        while len(q)>=2:
            s1 = -heapq.heappop(q)
            s2 = -heapq.heappop(q)
            diff = abs(s1-s2)
            if diff>0:
                heapq.heappush(q, -diff)
        return 0 if not q else -q[0]
        