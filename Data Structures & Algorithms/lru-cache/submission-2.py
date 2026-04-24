class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.n = 0
        self.data = {}
        self.timestamps = {}
        self.curr_time = 0
        self.q = collections.deque()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.timestamps[key] = self.curr_time
        self.q.append((self.curr_time, key))
        self.curr_time += 1
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            self.n += 1
        self.data[key] = value
        self.timestamps[key] = self.curr_time
        self.q.append((self.curr_time, key))
        self.curr_time += 1
        while self.n>self.capacity:
            qt, qkey = self.q.popleft()
            if self.timestamps[qkey] == qt:
                del self.data[qkey]
                del self.timestamps[qkey]
                self.n -= 1

