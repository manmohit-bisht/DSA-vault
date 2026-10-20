class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num  # because a^a = 0 and a^0 = a, all the numbers that appear twice will cancel each other out, leaving only the single number.
        return ans
