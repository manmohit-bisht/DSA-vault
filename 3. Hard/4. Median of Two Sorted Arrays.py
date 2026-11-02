# 2 pointers approach
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_length = m + n

        i, j = 0, 0
        mid = total_length // 2
        prev = 0
        curr = 0
        for k in range(
            mid + 1
        ):  # iterate mid + 1 times to reach the middle of the merged array
            prev = curr  # store the previous value of curr, since curr will be updated in the next step
            # check if i is within bounds and j is out of bounds or nums1[i] is less than or equal to nums2[j]
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if total_length % 2:
            return curr
        else:
            return (curr + prev) / 2


# an better approach and more efficient approach is to use binary search to find the median in O(log(min(m, n))) time complexity. Here is the implementation:
