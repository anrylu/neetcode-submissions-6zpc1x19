class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        pending_tasks = []
        for k, v in counter.items():
            heapq.heappush(pending_tasks, -v)
        cooldown_tasks = []
        cycles = 0
        while pending_tasks or cooldown_tasks:
            while cooldown_tasks and cooldown_tasks[0][0]<=cycles:
                _, v = heapq.heappop(cooldown_tasks)
                heapq.heappush(pending_tasks, -v)
            if pending_tasks:
                v = -heapq.heappop(pending_tasks)-1
                cycles += 1
                if v > 0:
                    heapq.heappush(cooldown_tasks, (cycles+n, v))
            elif cooldown_tasks:
                cycles = cooldown_tasks[0][0]

        return cycles
