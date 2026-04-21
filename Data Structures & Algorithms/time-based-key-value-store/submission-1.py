class TimeMap:

    def __init__(self):
        self.k2v = collections.defaultdict(list)
        self.k2t = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.k2v[key].append(value)
        self.k2t[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        import bisect
        if not self.k2v[key]:
            return ""
        i = bisect.bisect(self.k2t[key], timestamp)
        n = len(self.k2t[key])
        if i>=n:
            i = n - 1
        elif self.k2t[key][i] > timestamp:
            i = i - 1
            if i<0: return ""
        return self.k2v[key][i]
        
