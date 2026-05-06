class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        import bisect
        bisect.insort(self.nums, val)
        return self.nums[len(self.nums)-self.k]
        
