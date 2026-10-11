class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        mp = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in mp:
                mp[sorted_s] = [s]
            else:
                mp[sorted_s].append(s)

        res = []
        for key, value in mp.items():
            res.append(value)

        return res
