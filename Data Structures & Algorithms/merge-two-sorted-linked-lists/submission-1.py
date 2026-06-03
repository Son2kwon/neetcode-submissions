# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans: Optional[ListNode]

        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        # 초기값 세팅
        if list1.val < list2.val:
            cur = ListNode(list1.val, None)
            ans = cur
            list1 = list1.next
        else:
            cur = ListNode(list2.val, None)
            ans = cur
            list2 = list2.next
        
        head = ans

        while list1 and list2:
            if list1.val < list2.val:
                cur = ListNode(list1.val, None)
                ans.next = cur
                list1 = list1.next
                ans = ans.next
            else:
                cur = ListNode(list2.val, None)
                ans.next = cur
                list2 = list2.next
                ans = ans.next
        
        while list1:
            cur = ListNode(list1.val, None)
            ans.next = cur
            list1 = list1.next
            ans = ans.next

        while list2:
            cur = ListNode(list2.val, None)
            ans.next = cur
            list2 = list2.next
            ans = ans.next

        return head

  

# 전형적인 Merge Sort 방식이네요...
# 공간 복잡도 O(n + m)으로 푸는 게 가장 단순할 것 같다.