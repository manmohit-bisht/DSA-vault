class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while True:
            if slow == fast:
                break
            slow = nums[slow]
            fast = nums[fast]

        return slow


# solution using set -> can be done altohugh it will take O(n) space complexity
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        visited = set()

        index = 0
        while True:
            if nums[index] not in visited:
                visited.add(nums[index])
                index = nums[index]
            else:
                return nums[index]
