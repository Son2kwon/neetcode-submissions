# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def LCA(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 같은 방향으로 넘어간다면 -> 넘어가는 방향으로 LCA 재귀
        if p.val < node.val and q.val < node.val:
            return self.LCA(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return self.LCA(node.right, p, q)
        # 같은 방향으로 움직이지 않는다면 -> 좌우로 벌어지거나, 하나는 움직이지 않거나 = not(다른 방향으로 넘어가는 경우)
        else:
            return node
        
        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.LCA(root, p, q)
        
# BST니까 좀 찾기는 편한 것 같은데, p랑 q의 포인터를 어떻게 움직이고, ancestor는 어떻게 인식할거냐는게 문제인데
# 어떤 노드를 기준으로 p와 q가 모두 left 또는 Right로 움직인다면, ancestor도 같이 내려가야 함
# 만약 하나는 left, 하나는 right으로 간다면? LCA는 그 노드가 될 것.

# Tree니까 재귀적으로 이동한다면
#   Base case: p와 q가 같은 방향으로 움직이지 않을 시, 현 노드를 반환
#   같은 방향으로 움직인다면, p와 q와 ancestor 모두 움직인다.