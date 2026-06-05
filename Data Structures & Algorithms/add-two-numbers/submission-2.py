# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1, None); cur = ans

        carry = 0

        while l1 and l2:
            a = l1.val; b = l2.val; result = a + b + carry
            if result >= 10: 
                carry = 1
                result -= 10
            else:
                carry = 0

            cur.next = ListNode(result)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            result = l1.val + carry
            print(result)
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0
            cur.next = ListNode(result)
            cur = cur.next
            l1 = l1.next

        while l2:
            result = l2.val + carry
            if result >= 10:
                carry = 1
                result -= 10
            else:
                carry = 0
            cur.next = ListNode(result)
            cur = cur.next
            l2 = l2.next

        if carry == 1:
            cur.next = ListNode(1)

        return ans.next

# 그냥 덧셈하면 될 것 같은데?
# 자릿수가 같으면 이렇게 풀면 되는데, 자릿수가 다르다면...
