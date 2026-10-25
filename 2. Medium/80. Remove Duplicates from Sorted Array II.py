class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        left = 1

        for right in range(2, n):
            if nums[right] != nums[left - 1]:
                left += 1
                nums[left] = nums[right]

        return left + 1
