# beats 5% in time and 10% in space
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        
        curr = head
        last = head
        while curr:
            mcount = m
            ncount = n
            while curr and mcount != 0:
                last = curr         # we store curr node in last bc we mod curr in next line
                curr = curr.next    # we move on to th next node
                mcount -= 1

            while curr and ncount != 0:
                curr = curr.next # we move on to next node and do not store last 
                ncount -= 1
            last.next = curr # we only update last after going through one cycle of m and n 
        return head  