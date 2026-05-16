class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary: defaultdict[tuple, List[str]] = defaultdict(list)

        for string in strs:
            alphabet = [0] * 26

            for c in string:
                alphabet[ord(c) - ord('a')] += 1

            dictionary[tuple(alphabet)].append(string)

        ans: List[List[str]] = []

        for strings in dictionary.values():
            ans.append(strings)

        return ans