class Solution:
    def total_time(self, arr, k):
        total_time = 0
        for pile in arr:
            total_time += (pile + k - 1) // k
        return total_time

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_pile = 1
        max_pile = max(piles)
        ans = max_pile

        while min_pile <= max_pile:
            k = (max_pile + min_pile) // 2
            if self.total_time(piles, k) <= h:
                ans = k
                max_pile = k - 1
            else:
                min_pile = k + 1

        return ans
