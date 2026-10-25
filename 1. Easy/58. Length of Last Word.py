class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n - 1, -1, -1):
            if s[i] == " " and count == 0:
                continue
            if s[i] == " " and count != 0:
                break

            count += 1

        return count
