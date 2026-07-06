# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def DFS(self, l: list, node: Optional[TreeNode]):
        if node == None:
            l.append("1")
            l.append("#")
            l.append("@")
            return

        cur_val = str(node.val)
        l.append(len(cur_val))
        l.append(cur_val)
        l.append("@")

        self.DFS(l, node.left)
        self.DFS(l, node.right)

    def build(self, s: str, p: int) -> (Optional[TreeNode], int):
        if p > len(s):
            return None, p

        if s[p + 1] == "#":
            p += 3
            return None, p

        cur_val = 0

        negative = False
        if s[p] == '-':
            negative = True

        p += 1

        while s[p] != "@":
            cur_val = cur_val * 10 + int(s[p])
            p += 1
        p += 1

        if negative:
            cur_val *= -1

        node = TreeNode(cur_val)
        node.left, p = self.build(s, p)
        node.right, p = self.build(s, p)

        return node, p

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lst = []
        self.DFS(lst, root)
        return "".join(map(str, lst))
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        return (self.build(data, 0))[0]

# 계속했던 트리의 직렬화
#   빈 공간에 null 같은 빈 공간을 명시해주는 것이 중요하다.

# Serialize
#   반환값이 str이니까..
#   [길이] + [데이터] + [구분자 @]
#   Null은 # 로 표현할까
#   string을 한 번에 만들지 말고, list에 넣어둔 다음에 나중에 join

# Deserialize
#   포인터를 사용해서..
#   [데이터]를 숫자로 변환
#   [@] 다음부터 다시 시작

# Time Complexity: O(n), O(m); n is the number of nodes, m is the length of string
# Space Complexity: O(h), O(n)