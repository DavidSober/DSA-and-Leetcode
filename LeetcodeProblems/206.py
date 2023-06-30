# although this method is not as clean as the first this one makes the most sense
# if you draw it out 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            NN = curr.next
            curr.next = prev
            prev = curr
            curr = NN
        return prev


# this is the fastest and easiest way to reverse a linked list from what I have seen...
# beats 66% in time and 78% in space

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next
        return prev