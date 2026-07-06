# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def DFS(self, s: str, node: Optional[TreeNode]) -> str:
        if node == None:
            return s + "#@"

        return s + str(node.val) + "@" + self.DFS(s, node.left) + self.DFS(s, node.right)

    def build(self, s: str, p: int) -> (Optional[TreeNode], int):
        if p > len(s):
            return None, p

        if s[p] == "#":
            p += 2
            return None, p

        cur_val = 0

        while s[p] != "@":
            cur_val = cur_val * 10 + int(s[p])
            p += 1
        p += 1

        node = TreeNode(cur_val)
        node.left, p = self.build(s, p)
        node.right, p = self.build(s, p)

        return node, p

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = ""
        return self.DFS(s, root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return (self.build(data, 0))[0]

# 계속했던 트리의 직렬화
#   빈 공간에 null 같은 빈 공간을 명시해주는 것이 중요하다.

# Serialize
#   반환값이 str이니까..
#   [데이터] + [구분자 @]
#   Null은 # 로 표현할까

# Deserialize
#   포인터를 사용해서..
#   [데이터]를 숫자로 변환
#   [@] 다음부터 다시 시작