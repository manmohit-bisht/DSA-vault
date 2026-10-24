class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        ans = nums[0]
        curr = 0

        for i in range(n):
            curr += nums[i]
            ans = max(ans, curr)
            if curr < 0:
                curr = 0

        return ans
