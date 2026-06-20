# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans: int = 0

    def diameter(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        l_height = self.diameter(node.left)
        r_height = self.diameter(node.right)

        self.ans = max(self.ans, l_height + r_height)

        return max(l_height, r_height) + 1

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root)

        return self.ans
        
# Diameter라고 생각해서 어렵지 height라고 생각하면...

# 각 node를 포함하는 가장 긴 path는 height(node.left) + height(node.right)
