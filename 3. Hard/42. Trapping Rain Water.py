class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        max_height = 0
        for i in range(n):
            if height[max_height] < height[i]:
                max_height = i

        total_water = 0
        local_max = height[0]
        for i in range(1, max_height):
            if height[i] < local_max:
                total_water += local_max - height[i]
            else:
                local_max = height[i]

        local_max = height[n - 1]
        for i in range(n - 2, max_height, -1):
            if height[i] < local_max:
                total_water += local_max - height[i]
            else:
                local_max = height[i]
        return total_water


# --> Two Pointer Approach


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        total_water = 0
        left_maxima, right_maxima = height[0], height[n - 1]

        while left < right:
            if height[left] < height[right]:
                if height[left] < left_maxima:
                    total_water += left_maxima - height[left]
                else:
                    left_maxima = height[left]
                left += 1
            else:
                if height[right] < right_maxima:
                    total_water += right_maxima - height[right]
                else:
                    right_maxima = height[right]
                right -= 1
        return total_water
