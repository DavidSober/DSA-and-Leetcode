# The non commented version is a slighly faster version that I figured out 
# the commented version is the slower but initial solution i came up with
# beats 70% in time and 12% in time 
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # main idea here it to do an in order traversal for the BST to return a list of what should be sorted node.vals
        # acending order (since that is a property of BSTs and in order dfs), however since the BST is almost sorted
        # we will get an almost sorted list in vals. After this we can compare vals to a sorted version of vals
        # to find the problematic node.vals aka the nodes that were switched. Then all we have to do is switch those 
        # vals and the problem is solved 
        vals = []
        def dfs(node): 
            if not node:
                return 
            dfs(node.left)
            vals.append(node) # first do dfs in order to return an almost sorted list
            dfs(node.right)
            return 
        dfs(root)
        sortedvals = sorted(vals, key=lambda x: x.val) # we sort the vals by the value of the nodes
        switch = [] 
        for x, y in zip(vals, sortedvals): # we now find the two nodes that need to be switched by comparing vals to the sorted version of itself 
            if x != y: # if a node in vals does not equal the sorted val in sortedvals we know that node should be switched
                switch.append(x)
        switch[0].val, switch[1].val = switch[1].val, switch[0].val # now that we found the vals to switch we do so.
            

# beats 20% in time and 12% in space
    # def recoverTree(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     vals = []
    #     def dfs(node):
    #         if not node:
    #             return 
    #         dfs(node.left)
    #         vals.append(node.val)
    #         dfs(node.right)
    #         return 
    #     dfs(root)
    #     sortedvals = sorted(vals)
    #     switch = []
    #     for x, y in zip(vals, sortedvals):
    #         if x != y:
    #             switch.append(x)
    #     count = 0
    #     def switching(node):
    #         nonlocal count
    #         if not node:
    #             return 
    #         if count == 2: # once we have switched twice we are done and should stop recursing
    #             return 
    #         if node.val in switch:
    #             for i in switch:
    #                 if node.val != i:
    #                     count += 1
    #                     node.val = i
    #                     break       # to prevent multiple switching we must break out of the loop after one switch
                        
    #         switching(node.left)
    #         switching(node.right)
    #         return
    #     switching(root)
    #     print(count)
            