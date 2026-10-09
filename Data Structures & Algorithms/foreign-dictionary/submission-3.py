class Solution:
    def findDiff(self, i_word: str, j_word: str) -> [int, int]:
        i_index = 0; i_len = len(i_word)
        j_index = 0; j_len = len(j_word)

        while i_index < i_len and j_index < j_len:
            if i_word[i_index] == j_word[j_index]:
                i_index += 1
                j_index += 1
            else:
                return [i_index, j_index]

        # 다른 글자가 없고, 앞 단어가 짧거나 같을 때: 정상적인 경우지만 정보 없음
        if i_len <= j_len and i_index == i_len:
            return [-1, -1]

        # 불가능한 경우: 
        if i_index < i_len and j_index == j_len:
            return [-2, -2]

    def topologicalSort(self, d: dict, degree: defaultdict):
        l = []
        s = deque()

        for n in d.keys():
            if degree[n] == 0: s.append(n)

        while len(s) != 0:
            n = s.popleft()
            l.append(n)

            # n을 뺐으니까, 그 n에서 이어지는 node들의 degree--
            for neighbor in d.get(n, []):
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    s.append(neighbor)

        # 모든 노드가 다 들어가있으면 정상
        if len(l) == len(d.keys()): return l
        # 아니라면 error ->  빈 문자열
        else: return []

    def foreignDictionary(self, words: List[str]) -> str:
        d = dict(); n = len(words)
        inDegree = defaultdict(int)

        # 모든 글자들에 대한 노드 만들어두기
        for word in words:
            for c in word:
                d[c] = []

        for i in range(n - 1):
            j = i + 1
            i_index, j_index = self.findDiff(words[i], words[j])
            
            if i_index == -1 and j_index == -1: continue
            elif i_index == -2 and j_index == -2: return ""

            l_first = words[i][i_index]; l_last = words[j][j_index]

            if l_last not in d[l_first]:
                d[l_first].append(l_last)
                inDegree[l_last] += 1
        
        ans = self.topologicalSort(d, inDegree)

        return ''.join(ans)

# words를 보고, 글자의 순서를 알아내라는 말이구나.

# 결국 단어 2개를 골라서, 다른 부분을 찾은 후, 그 순서를 확정하라는 말인데
# O(n^2)으로 푸는 방법이 하나 있을테고
# 이 문제가 graph에 있는 이유가 있는 것 같은데, 각 문자를 node, 순서 관계를 directed edge로 본다면...

# lixcially 먼저인 character -> 나중인 character가 있을 때
# 가장 첫 문자부터 출발해서 하나씩 연결하면 나오긴 하겠다.

# 힌트 1: Graph 문제로 생각해보면, node는 문자들, edge는 뭘까? 
#   이미 위에서 한 게 이런 내용이고, 그러면 방향은 맞은 것 같은데
# 지금 문제인 건 첫번째 노드를 어떻게 찾냐인데
# 이거 Topological sort 하면 되는 거 아닌가?

# Topological Sort by Kahn's algorithm

# O(|V|) -> O(26) = O(1)
# O(|E|) -> O(26 * 25) = O(1)

# Time Complexity: O(n^2 * L); L is the maximum length of word in words
# Space Complexity: O(|V| + |E|)