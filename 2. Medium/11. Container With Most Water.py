class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1

        res = 0
        while i < j:
            width = j - i
            actual_height = min(height[i], height[j])
            area = actual_height * width
            res = max(res, area)

            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

        return res
