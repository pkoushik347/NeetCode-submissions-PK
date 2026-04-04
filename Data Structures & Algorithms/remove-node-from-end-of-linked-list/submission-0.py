# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = head

        k = 0
        while (head):
            k += 1
            head = head.next
        # print(k)
        if (n == k):
            return temp.next
        n = k - n -1
        i = 0
        while (curr):
            if (i == n):
                curr.next = curr.next.next
            curr = curr.next
            i += 1
        return temp