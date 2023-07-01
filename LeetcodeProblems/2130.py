# fast and slow pointer to get to the middle of the list
# then reverse the second half of the list 
# then make a start pointer at the head and traverse with start and prev
# add their vals at each step and log the max val then return
# beats 87% in time and 77% in space


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now halfway through list
        prev = None
        while slow: # reverse second half of list
            NN = slow.next
            slow.next = prev
            prev = slow
            slow = NN
        # at this point prev points to the last node in the list and 
        # the second half of the list is reversed
        start = head
        ans = 0
        while prev:
            ans = max(ans, start.val + prev.val)
            prev = prev.next
            start = start.next
        return ans