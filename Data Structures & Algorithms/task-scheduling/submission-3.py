class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        ans = 0; max_freq = float('-inf');
        countOfMax = -1 # 처음 들어오는 애 방지하기 위해 -1로 시작
        for value in c.values():
            if max_freq < value:
                max_freq = value
                
        for value in c.values():
            if max_freq == value:
                countOfMax += 1

        ans = max_freq + n * (max_freq - 1) + countOfMax


        return max(ans, len(tasks))

# 가장 많이 나오는 놈이 지배적이다

# 가장 많이 나오는 애를 먼저 배치 -> len = 개수 + n * (개수 - 1)
# 가장 많이 나오는 애가 여러명이면 -> len += 1
# ans는 idle이 필요할 때의 길이, len(tasks)은 idle이 필요없을 때의 길이

# Time Complexity: O(n); n is the length of tasks
# Space Complexity: O(k); k is the number of tasks