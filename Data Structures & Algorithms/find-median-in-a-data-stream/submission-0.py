class MedianFinder:

    def __init__(self):
        self.n = 0
        self.top_half = []
        self.bottom_half = []

    def addNum(self, num: int) -> None:
        self.n += 1
        if not self.top_half or num>self.top_half[0]:
            heapq.heappush(self.top_half, num)
        else:
            heapq.heappush(self.bottom_half, -num)
        while len(self.top_half)>(self.n+1)//2:
            heapq.heappush(self.bottom_half, -heapq.heappop(self.top_half))
        while len(self.bottom_half)>self.n//2:
            heapq.heappush(self.top_half, -heapq.heappop(self.bottom_half))

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.top_half[0]
        else:
            return (self.top_half[0]-self.bottom_half[0])/2
        
        