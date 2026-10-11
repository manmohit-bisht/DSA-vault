class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracked = {}
        n = len(nums)

        for i in range(n):
            rem = target - nums[i]
            if rem in tracked:
                return [i, tracked[rem]]
            tracked[nums[i]] = i