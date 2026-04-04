class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left<right:
            v = numbers[left] + numbers[right]
            if v == target:
                return [left+1, right+1]
            elif v > target:
                right -= 1
            else: 
                left += 1
        return []
        
   