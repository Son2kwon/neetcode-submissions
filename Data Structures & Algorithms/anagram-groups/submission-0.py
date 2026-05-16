class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary: dict[tuple, List[str]] = {}

        for string in strs:
            counter = tuple(sorted(Counter(string).items()))

            if counter in dictionary:
                dictionary[counter].append(string)
            else:
                dictionary[counter] = [string]

        ans: List[List[str]] = []

        for strings in dictionary.values():
            ans.append(strings)

        return ans