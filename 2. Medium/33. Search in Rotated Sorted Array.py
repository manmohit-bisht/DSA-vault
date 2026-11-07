# fmt: off
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left<=right:
            mid = (left+right) // 2
            if nums[mid] ==  target:
                return mid
            
            #check left sorted portion of the array
            if nums[mid] >= nums[left]:
                if target < nums[left] or target > nums[mid]: # check if target is not in the left sorted portion
                    left = mid + 1
                else:
                    right = mid-1
            #check right sorted portion of the array
            else:
                if target > nums[right] or target < nums[mid]: # check if target is not in the right sorted portion
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
