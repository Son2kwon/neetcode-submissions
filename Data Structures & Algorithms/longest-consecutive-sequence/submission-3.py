class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        
        for i in nums:
            count = 1
            if i - 1 not in nums:
                while i + 1 in nums:
                    count += 1
                    i += 1

            ans = max(count, ans)

        return ans


# sorting 한 다음에 그냥 세면 되지 않을까? 그러면 O(n log n)으로 풀 수 있어. 근데 문제 조건에 O(n)이라 적혀있네
# 그래도 입력 가능한 수에 비해서 입력이 작은데 그러면 해시 테이블로 접근할 수 있지 않을까? 특히 딕셔너리로
# 각 원소를 시작점으로 잡았을 때, 얼만큼 갈 수 있는지를 ans에 저장, 그 중 max를 내보내는 방법도 되겠다.
# Time Complexity: O(n^2)
# Space Complexity: O(n)