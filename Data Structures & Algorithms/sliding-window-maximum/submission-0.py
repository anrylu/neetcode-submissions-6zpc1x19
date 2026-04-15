class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ret = [-q[0][0]]
        for right in range(k, n):
            heapq.heappush(q, (-nums[right], right))
            if (right-left+1)>k:
                left += 1
            while q and q[0][1]<left:
                heapq.heappop(q)
            ret.append(-q[0][0])
        return ret