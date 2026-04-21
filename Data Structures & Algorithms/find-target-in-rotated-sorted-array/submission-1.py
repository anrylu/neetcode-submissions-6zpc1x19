class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # find pivot
        low = 0
        high = n-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[n-1]:
                low = mid + 1
            else:
                high = mid
        pivot = low

        # find target
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            pos = (mid+pivot+n)%n
            if nums[pos]==target:
                return pos
            elif nums[pos]>target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
