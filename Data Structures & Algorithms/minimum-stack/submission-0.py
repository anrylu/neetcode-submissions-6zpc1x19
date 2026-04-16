class MinStack:

    def __init__(self):
        self.stack = []
        self.q = []
        self.existing = collections.Counter()

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.q, val)
        self.existing[val] += 1
        
    def pop(self) -> None:
        if self.stack:
            self.existing[self.stack[-1]] -= 1
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        while self.q and self.existing[self.q[0]] == 0:
            heapq.heappop(self.q)
        return self.q[0]
        
