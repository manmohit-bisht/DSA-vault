class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        setB = set(nums2)
        common = set()

        for num in nums1:
            if num in setB:
                common.add(num)

        return list(common)


"""
you can simply use intersection of sets -: 
return list(set(nums1) & set(nums2)) or 
return list(set(nums1).intersection(set(nums2)))
"""
