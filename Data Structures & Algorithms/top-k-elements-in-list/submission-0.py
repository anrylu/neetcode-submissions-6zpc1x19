class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = collections.Counter(nums)
        buckets = [[] for _ in range(n+1)]
        for num, count in counter.items():
            buckets[count].append(num)
        ret = []
        for count in range(n, 0, -1):
            for num in buckets[count]:
                ret.append(num)
                if len(ret)>=k:
                    return ret
        return ret

