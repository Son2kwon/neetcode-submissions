class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            n = len(s)
            encoded_str = encoded_str + str(n) + "#" + s

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i: int = 0
        ans = []

        while s:
            if s[i] == "#":
                n = int(s[0:i])
                decoded_str = s[i + 1: i + 1 + n]
                ans.append(decoded_str)
                s = s[i + 1 + n:]
                i = 0
            else:
                i += 1

        return ans