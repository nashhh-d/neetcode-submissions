import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        # Put first node of every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:

            # Take smallest
            val, i, node = heapq.heappop(heap)

            # Put it in answer
            curr.next = node
            curr = curr.next

            # Add next node from same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next