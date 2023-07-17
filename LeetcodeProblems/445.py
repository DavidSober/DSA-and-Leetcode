# beats 50% in time and 68% in space
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1:
            n1.append(l1.val)
            l1 = l1.next
        n2 = []
        while l2:
            n2.append(l2.val)
            l2 = l2.next
        n1 = int("".join([str(n) for n in n1]))
        n2 = int("".join([str(n) for n in n2]))
        ans = n1 + n2
        ans = [int(n) for n in str(ans)]
        ret = ListNode()
        head = ret
        for num in ans:
            new = ListNode(num)
            ret.next = new
            ret = ret.next
        return head.next