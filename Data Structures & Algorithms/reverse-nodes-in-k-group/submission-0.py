# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find the kth node
            kth = groupPrev

            for i in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            # Node after the group
            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part to reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp