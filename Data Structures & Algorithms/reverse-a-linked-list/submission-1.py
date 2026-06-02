# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur: Optional[ListNode] = head
        if cur == None: return None
        next_node: Optional[ListNode] = cur.next
        if next_node == None: return cur
        next_next_node: Optional[ListNode] = next_node.next
        cur.next = None

        while next_next_node != None:
            next_node.next = cur
            cur = next_node
            next_node = next_next_node
            next_next_node = next_node.next

        next_node.next = cur

        return next_node
        
    
# Singly Linked List라 함부로 접근하기 어렵네... 이중 루프로 돌리면 편하긴 한데
# 앞으로 두 번을 내다보면 해결되긴 한다.