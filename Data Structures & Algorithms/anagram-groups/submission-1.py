class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary: dict[tuple, List[str]] = {}

        for string in strs:
            alphabet = [0] * 26

            for c in string:
                alphabet[ord(c) - ord('a')] += 1

            if tuple(alphabet) in dictionary:
                dictionary[tuple(alphabet)].append(string)
            else:
                dictionary[tuple(alphabet)] = [string]

        ans: List[List[str]] = []

        for strings in dictionary.values():
            ans.append(strings)

        return ans