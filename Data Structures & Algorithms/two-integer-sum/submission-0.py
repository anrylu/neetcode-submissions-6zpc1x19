class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v2p = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in v2p:
                return [v2p[diff], i]
            v2p[num] = i
        return []