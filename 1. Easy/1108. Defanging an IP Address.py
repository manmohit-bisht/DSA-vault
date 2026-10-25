class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        n = len(address)

        for i in range(n):
            if address[i] == ".":
                ans += "[.]"
            else:
                ans += address[i]

        return ans
