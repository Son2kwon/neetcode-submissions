# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def change(self, node: Optional[TreeNode]):
        if node == None:
            return

        tmp = node.left
        node.left = node.right
        node.right = tmp

        self.change(node.left)
        self.change(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.change(root)

        return root

# Tree는 내가 잘 못 다루는 자료구조지만 여기서 연습하라는 거지 뭐.

# Time Complexity: O(n); n is the number of nodes
# Space Complexity: O(h); h is the height of tree