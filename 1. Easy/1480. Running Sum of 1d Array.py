class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running_sum = 0
        n = len(nums)

        for i in range(n):
            running_sum += nums[i]
            nums[i] = running_sum
        
        return nums