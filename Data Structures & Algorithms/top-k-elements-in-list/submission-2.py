class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary: defaultdict[int, int] = defaultdict(int)
        n = len(nums)

        bucket:List[List[int]] = [ [] for _ in range(0, n+1) ]

        for i in nums:
            dictionary[i] += 1

        for key, values in dictionary.items():
            bucket[values].append(key)

        ans = []

        for i in range (n, 0, -1):
            if len(bucket[i]) != 0:
                ans = ans + bucket[i]
            
            if len(ans) == k:
                break
        
        return ans

        

# Time Complexity: O(n log n)
# Space Complexity: O(k)