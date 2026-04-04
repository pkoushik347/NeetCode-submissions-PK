# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr =[]
        while (head != None):
            arr.append(head.val)
            head = head.next
        dummy = ListNode(0, None)
        k = dummy
        for i in arr[::-1]:
            dummy.next = ListNode(i, None)
            dummy = dummy.next
        return k.next
