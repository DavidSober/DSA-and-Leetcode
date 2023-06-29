# recursive approach
# beats 78% in time and 30% in space

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rec(node):
            if not node or not node.next:
                return node
            
            NN = node.next
            node.next = rec(node.next.next)
            NN.next = node

            return NN
        return rec(head)
    


# Iterative approach
# beats 99% in time and 100% in space

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head

        dummy = head.next  # if we have accomplished the goal head.next will be the start of the pair reversed linked list            
        prev = None                     
        while head and head.next:
            if prev:
                prev.next = head.next # connects the previous pair to the rest of the list (connects node 0 to node 3)
            
            prev = head # updates prev to be the current head bc later the current head will be previous
                        # we need to update prev to do the step in the if statement above

            next_node = head.next.next # if head was 1 this would point to 3
            head.next.next = head # should reverse the pair

            head.next = next_node # makes head node 1 point to node 3
            head = next_node # move onto next pair

        return dummy
