class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary: defaultdict[int, int] = defaultdict(int)

        for i in nums:
            dictionary[i] += 1

        dictionary = sorted(dictionary.items(), key=lambda x : x[1], reverse=True)

        ans = []

        for key, values in dictionary:
            ans.append(key)

        return ans[0:k]

# Time Complexity: O(n log n)
# Space Complexity: O(k)