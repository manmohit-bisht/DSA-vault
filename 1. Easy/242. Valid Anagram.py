class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            chars[ord(s[i]) - ord("a")] += 1
            chars[ord(t[i]) - ord("a")] -= 1

        for num in chars:
            if num != 0:
                return False
        return True
