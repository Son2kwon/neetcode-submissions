# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def DFS (self, node: Optional[TreeNode]) -> int:
        l_depth = 0; r_depth = 0
        if node.left:
            l_depth = self.DFS(node.left)
        if node.right:
            r_depth = self.DFS(node.right)

        return max(l_depth, r_depth) + 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.DFS(root)

        
        
# 그냥 DFS로 depth를 구하는게...

# Time Complexity: O(n)
# Space Complexity: O(h)