class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        st = set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        return False
