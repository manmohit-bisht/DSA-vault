class Solution:
    def canGive(self, candies, k, m):
        given = 0
        for pile in candies:
            given += pile // m
            if given >= k:
                return True
        return False

    def maximumCandies(self, candies: list[int], k: int) -> int:
        min_candy = 1
        max_candy = max(candies)

        while min_candy <= max_candy:
            mid = (min_candy + max_candy) // 2
            if self.canGive(candies, k, mid):
                min_candy = mid + 1
            else:
                max_candy = mid - 1

        return max_candy
