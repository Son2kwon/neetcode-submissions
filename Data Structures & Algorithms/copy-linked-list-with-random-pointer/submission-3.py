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
        if head == None:
            return None
        # 1단계: 리스트 복사        
        cur = head

        while cur:
            new_Node = Node(cur.val)
            
            nxt = cur.next
            cur.next = new_Node
            new_Node.next = nxt

            cur = nxt
        
        # 2단계: random 연결
        cur = head

        while cur:
            rand = cur.random

            if rand == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next

        

            cur = cur.next.next

        # 3단계: 리스트끼리 새로 연결
        new_head = head.next
        new_cur = new_head; cur = head

        while cur:
            # 기존 리스트의 nxt
            nxt = new_cur.next
            # 연결
            cur.next = nxt
            if nxt != None:
                new_cur.next = nxt.next
            else:
                new_cur.next = nxt
            # 이동
            cur = cur.next
            new_cur = new_cur.next


        return new_head
        

# 공간 복잡도 O(1)의 풀이
# 기존 리스트 사이사이에 복사본을 넣는다. -> 1 loop
# 리스트를 훑으면서 random을 연결한다. -> 2 loop
# new_head를 정하고, 새로운 리스트들끼리 연결한다 -> 3 loop