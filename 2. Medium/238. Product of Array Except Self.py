class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [1] * n

        #prefix product
        prefix = 1
        for i in range(n):
            arr[i] = prefix
            prefix *= nums[i]
        #suffix product
        suffix = 1
        for i in range(n-1,-1,-1):
            arr[i] *= suffix
            suffix *= nums[i]
        return arr