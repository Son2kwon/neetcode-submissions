class WordDictionary:
    root: dict

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur:
                cur[ch] = {}

            cur = cur[ch]

        cur["*"] = True


    def DFS(self, word: str, i: int, node: dict) -> bool:
        if i == len(word):
            if "*" in node:
                return True
            else:
                return False

        ch = word[i]

        if ch == ".":
            truth = []
            for children in node:
                if children == "*":
                    continue
                truth.append(self.DFS(word, i + 1, node[children]))

            return any(truth)

        else:
            if ch in node:
                return self.DFS(word, i + 1, node[ch])
            else:
                return False

    def search(self, word: str) -> bool:
        return self.DFS(word, 0, self.root)
        
# 결국 진짜 단어사전을 만들라고 하는구나.

# Trie 안에 어떻게든 "."을 넣어보려 했는데, 안 된다. 그냥 set에 단어 전부 저장해두고 찾아볼까.