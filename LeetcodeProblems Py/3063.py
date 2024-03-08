# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        F = Counter(lst)
        lst = list(F.values())
        head = ListNode(lst[0])
        curr = head
        for num in lst[1:]:
            head.next = ListNode(num)
            head = head.next
        return curr