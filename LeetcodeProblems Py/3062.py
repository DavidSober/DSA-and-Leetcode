# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        curr = head
        even = 0
        odd = 0
        while curr:
            currE = curr.val
            currO = curr.next.val
            if currE > currO:
                even += 1
            elif currE < currO:
                odd += 1
            curr = curr.next.next
        if even > odd:
            return 'Even'
        elif odd > even:
            return 'Odd'
        return 'Tie'