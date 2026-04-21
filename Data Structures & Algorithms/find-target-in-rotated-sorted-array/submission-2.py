class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # find pivot
        low = 0
        high = n-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]<nums[n-1]:
                high = mid
            else:
                low = mid + 1
        pivot = low

        # search
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            pos = (mid+pivot)%n
            if nums[pos] == target:
                return pos
            elif nums[pos] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

