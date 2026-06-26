# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 만약 둘 다 None 이라면 True
        if p == None and q == None:
            return True
        # 하나만 None이라면 False
        elif (p == None and q != None) or (p != None and q == None):
            return False
        # 둘 다 존재한다면 비교 시작
        else:
            return (p.val == q.val) and self.check(p.left, q.left) and self.check(p.right, q.right)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)
# 현재 노드의 값이 같고, 왼쪽 서브트리가 서로 같은지, 오른쪽 서브트리가 서로 같은지 확인

# Time Complexity: O(n)
# Space Complexity: O(n)