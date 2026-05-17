class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        lst: List[str] = []
        for s in strs:
            n = len(s)
            lst.append(str(n) + "#" + s)
        print(encoded_str.join(lst))
        return encoded_str.join(lst)

    def decode(self, s: str) -> List[str]:
        i: int = 0
        ans = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length: int = int(s[i : j])
            decoded_str = s[j + 1: j + 1 + length]
            ans.append(decoded_str)
            i = j + 1 + length

        return ans

# Time Complexity: O(n): n = the number of strings / O(n): n = the length of string
# Space Complexity: O(n): n = length of the string / O(n): n = the number of strings