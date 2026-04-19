class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(reverse=True)
        reach_time = 0
        ret = 0
        for p, s in cars:
            next_reach_time = (target-p)/s
            if next_reach_time>reach_time:
                ret += 1
                reach_time = next_reach_time
        return ret
