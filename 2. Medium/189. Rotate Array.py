class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        n = len(nums)
        k = k % n  # effective rotations
        if k == n:  # if k=n, no need to rotate
            return

        left = 0
        while left < (
            n - k - 1
        ):  # bring the left pointer to the last element of the first part (i.e. the part that will be shifted to the right)
            left += 1

        i = left + 1
        while i < n:  # append the second part of the array to temp
            temp.append(nums[i])
            i += 1

        right = n - 1
        while left >= 0:  # move the first part of the array to the right
            nums[right] = nums[left]
            left -= 1
            right -= 1

        j = 0
        while j < len(temp):  # copy the elements of temp to the first part of the array
            nums[j] = temp[j]
            j += 1
