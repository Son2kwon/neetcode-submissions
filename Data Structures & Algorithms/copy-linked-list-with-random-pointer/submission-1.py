"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1, None, None)
        prev = dummy

        node_map = {}

        cur = head;
        while cur:
            new_Node = Node(cur.val, None, None)
            node_map[cur] = new_Node
            
            prev.next = new_Node
            prev = prev.next
            cur = cur.next

        cur = head; new_cur = dummy.next;

        while cur:
            if cur.random:
                new_cur.random = node_map[cur.random]

            cur = cur.next
            new_cur = new_cur.next


        return dummy.next
        

# 일단 공간 복잡도 O(n)의 풀이
# 
