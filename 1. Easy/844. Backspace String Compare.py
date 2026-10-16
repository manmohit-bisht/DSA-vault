class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        actual_s = []

        for ch in s:
            if ch == "#":
                if actual_s:
                    actual_s.pop()
            else:
                actual_s.append(ch)

        actual_t = []

        for ch in t:
            if ch == "#":
                if actual_t:
                    actual_t.pop()
            else:
                actual_t.append(ch)

        return actual_s == actual_t


"""
if ch == '#' and len(actual_s) != 0:
    actual_s.pop()
doesn't work because if ch is '#' and actual_s is empty, it would push '#' into actual_s and then the comparison would be wrong, what
"""
