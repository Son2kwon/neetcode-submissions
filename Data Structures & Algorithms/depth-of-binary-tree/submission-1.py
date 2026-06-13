# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS (self, node: Optional[TreeNode], depth: int) -> int:
        l_depth = 0; r_depth = 0
        if node.left:
            l_depth = self.DFS(node.left, depth + 1)
        if node.right:
            r_depth = self.DFS(node.right, depth + 1)

        return max(l_depth, r_depth) + 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.DFS(root, 1)

        
        
# 그냥 DFS로 depth를 구하는게...