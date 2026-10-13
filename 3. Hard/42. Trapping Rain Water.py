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
