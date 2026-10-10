class Solution:
    def findDiff(self, a: str, b: str) -> int:
        idx = 0; n = len(a)
        count = 0

        while idx < n:
            if a[idx] != b[idx]:
                count += 1
            
            idx += 1

        return count


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.insert(0, beginWord)
        n = len(wordList)

        d = dict();
        for word in wordList:
            d[word] = []

        # 여기에 이제 글자 하나 차이나는 애들 연결하는 로직 짜면 되는데
        for i in range(n):
            for j in range(n):
                if i == j: continue
                word1 = wordList[i]; word2 = wordList[j]
                count = self.findDiff(word1, word2)

                if count == 1 and word2 not in d[word1] and word1 not in d[word2]:
                    d[word1].append(word2)
                    d[word2].append(word1)

        print(d)

        q = deque(); visited = set()
        q.append([beginWord, 0])

        while q:
            cur, count = q.popleft()
            if cur in visited: continue
            count += 1
            if cur == endWord: 
                return count

            visited.add(cur)

            for n in d.get(cur, []):
                if n not in visited:
                    q.append([n, count])

        return 0

# 하루키 문제인가? 그거랑 비슷보이긴 하네
# 각 단어를 노드로 보고, 딱 하나 다른 애들을 edge로 연결
# endWord까지 도착하면 성공, 아니면 0
# 결국 BFS인가?

# 근데 딱 하나 다른 그걸 어떻게 찾지? 그것만 찾으면 다 될 것 같은데

# O(n^2)이면 전체적으로 연결이 가능은 하겠다.