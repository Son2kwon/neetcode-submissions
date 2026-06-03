# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s: {id(ListNode)} = set()

        while head:
            print(s)
            if id(head) in s:
                return True
            
            s.add(id(head))
            head = head.next

        return False
        
# Cycle detection의 구현이네요

# 주소값을 set에 넣으면서 검사하다보면 금방 되긴 할 것 같은데