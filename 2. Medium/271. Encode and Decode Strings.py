class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for word in strs:
            size = len(word)
            encoded_str += str(size) + "#" + word
        return encoded_str

    def decode(self, s: str) -> list[str]:
        decoded_str = []
        n = len(s)
        i = 0
        while i < n:
            size = 0
            temp = ""
            while s[i] != "#":
                temp += s[i]
                size = int(temp)
                i += 1
            i += 1

            counter = 0
            word = ""
            while counter < size:
                word += s[i]
                counter += 1
                i += 1
            decoded_str.append(word)

        return decoded_str
