# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (not lists):
            return None
        pq = []
        dn = ListNode()
        curr = dn
        k = 0
        for i in lists:
            if (i):
                heapq.heappush(pq, (i.val, k, i))
                k += 1
        while (pq):
            val, _, node = heapq.heappop(pq)
            curr.next = node
            if (node.next):
                heapq.heappush(pq, (node.next.val, k, node.next))
                k += 1
            curr = curr.next
        return dn.next
        
        