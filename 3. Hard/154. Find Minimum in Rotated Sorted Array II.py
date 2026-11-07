class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:  # since if nums[mid] == nums[right], we cannot determine which side is sorted, so we reduce the search space by moving right pointer
                right -= 1

        return nums[right]
