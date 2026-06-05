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
        prev = dummy; cur = head

        while cur:
            new_node = Node(cur.val, None, None)
            prev.next = new_node
            cur = cur.next
            prev = prev.next

        cur = dummy.next; head_cur = head

        while head_cur:
            if head_cur.random == None:
                cur.random = None
            else:
                new_head = head; count = 0;

                while new_head != head_cur.random:
                    count += 1
                    new_head = new_head.next

                new_cur = dummy.next
                for _ in range(0, count):
                    new_cur = new_cur.next

                cur.random = new_cur

            
            head_cur = head_cur.next
            cur = cur.next

        return dummy.next
        

# 이건 뭔 소리래... 그냥 deep copy 하라는 소리인가..?
# parameter에 head.next 라든지 head.random 을 쓰면 안된다는 소리였구나.
# 근데 이렇게 보니까 next 연결은 쉬운데 random 연결이 어렵네.
# Node.val 도 범위가 작으니까, 그냥 hash table에 노드 저장해놓고 쓸까?
# 그렇게 풀기에는 Node values are not guaranteed to be unique라 되어있네. 꼼수 차단...

# Random을 어떻게 처리할 것인가
# Time Complexity가 O(n^2)으로 처리하면 되긴 할텐데...
