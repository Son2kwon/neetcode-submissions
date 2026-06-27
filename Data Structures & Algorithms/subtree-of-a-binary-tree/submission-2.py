# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.check(root, subRoot):
            return True
        else:
            if root == None and subRoot == None:
                return True
            elif (root == None and subRoot != None) or (root != None and subRoot == None):
                return False
            else:
                return self.search(root.left, subRoot) or self.search(root.right, subRoot)

    def check(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        else:
            return (p.val == q.val) and self.check(p.left, q.left) and self.check(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.search(root, subRoot)

# 마찬가지로 DFS로 접근하면 될 것 같은데
# 일단 val이 같은 node를 먼저 찾고, 거기서부터 체크하면 될 것 같다.

# 라고 생각했는데 [1,1] [1] 같은 케이스는 못 걸러내는구나.

# 아, 그냥 root부터 비교하면서, Subroot가 있는지만 확인하면 되는구나?
# 만약 val이 같가면 check 메소드로 확인, 만약 있다면 return True
#   check 메소드 결과 False라면, left로 내려가서 확인, right로 내려가서 확인