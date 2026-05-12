class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        pending_tasks = []
        for k, v in counter.items():
            heapq.heappush(pending_tasks, -v)
        colldown_tasks = []

        cycles = 0
        while pending_tasks or colldown_tasks:
            while colldown_tasks and colldown_tasks[0][0]<=cycles:
                _, v = heapq.heappop(colldown_tasks)
                heapq.heappush(pending_tasks, -v)
            if pending_tasks:
                v = -heapq.heappop(pending_tasks)-1
                cycles += 1
                if v>0:
                    colldown_tasks.append((cycles+n, v))
                continue
            else:
                cycles = colldown_tasks[0][0]
        return cycles
