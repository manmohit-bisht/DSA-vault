class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i < n - 2:
            while i != 0 and i < n - 2 and nums[i] == nums[i - 1]:
                i += 1
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                elif nums[j] + nums[k] < target:
                    j += 1
                    continue
                else:
                    k -= 1
                    continue

                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
            i += 1
        return ans
