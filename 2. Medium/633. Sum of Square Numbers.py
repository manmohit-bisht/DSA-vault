# fmt: off
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**0.5)
        nums = [x for x in range(n + 1)]  # 0 must be included, cause a and b can be 0 while finding c = a^2 + b^2

        left, right = 0, n
        while left <= right:
            curr_sum = nums[left] * nums[left] + nums[right] * nums[right]
            if curr_sum == c:
                return True
            elif curr_sum < c:
                left += 1
            else:
                right -= 1
        return False
