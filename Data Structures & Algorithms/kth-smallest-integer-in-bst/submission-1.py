# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count: int
    ans: int

    def __init__(self):
        self.count = 0
        self.ans = 0
    
    def traverseInOrder(self, node: Optional[TreeNode], k: int):
        if node == None:
            return None

        self.traverseInOrder(node.left, k)
        self.count += 1
        if k == self.count:
            self.ans = node.val
            return
        if self.count < k:
            self.traverseInOrder(node.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.traverseInOrder(root, k)

        return self.ans

# Heap으로 푸는 것도 아니고, BST로 이걸 풀라고..?
# 아, in-order로 순회하면 그게 순서 그대로구나?

# Time Complexity: O(k)
# Space Complexity: O(h)