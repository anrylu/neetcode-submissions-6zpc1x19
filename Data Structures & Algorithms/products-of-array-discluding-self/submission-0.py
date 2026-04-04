class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1]
        suffix_products = [1]
        for num in nums:
            prefix_products.append(prefix_products[-1]*num)
        for num in reversed(nums):
            suffix_products.append(suffix_products[-1]*num)
        
        n = len(nums)
        ret = []
        for i in range(n):
            ret.append(prefix_products[i]*suffix_products[n-i-1])
        return ret