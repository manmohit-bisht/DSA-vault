class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[0] <= nums[right]:
            return nums[0]

        min_element = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                min_element = min(min_element, nums[mid])
                right = mid - 1

        return min_element
