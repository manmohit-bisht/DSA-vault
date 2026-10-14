class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        n = len(s)
        left, right = 0, 0
        length = 0

        for right in range(n):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            length = max(length, right - left + 1)
            st.add(s[right])
            right += 1

        return length
