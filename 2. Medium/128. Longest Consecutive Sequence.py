class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        st = set(nums)
        visited = set()
        ans = 0

        for num in st:
            if num - 1 in st:
                continue

            length = 0
            i = 0
            while num + i in st:
                length += 1
                i += 1
            ans = max(ans, length)
        return ans
