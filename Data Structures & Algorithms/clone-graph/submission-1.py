"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    existed: dict

    def __init__(self):
        self.existed = {}

    def buildGraph(self, prev_node: Optional['Node'], org_node: Optional['Node']) -> Optional['Node']:
        new_node = Node(org_node.val)
        
        if new_node.val not in self.existed:
            self.existed[new_node.val] = new_node

        for node in org_node.neighbors:
            if node.val not in self.existed:
                new_neigh = self.buildGraph(new_node, node)
                new_node.neighbors.append(new_neigh)
            else:
                new_node.neighbors.append(self.existed[node.val])
        
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        root = self.buildGraph(None, node)

        return root

        
# 음.. DFS로 만들까 BFS로 만들까
# DFS로 만들면서 prev_node를 계속 가져간다는 마인드로 하면...

# 저 무한 재귀를 어떻게 해결할까...
# 아, set에 있으면 이웃에만 추가하면 되겠구나

# 근데 set으로 하니까 노드에 접근할 수 없으니, 딕셔너리로 구현한다면?
# 1 - 2
# 3 - 4