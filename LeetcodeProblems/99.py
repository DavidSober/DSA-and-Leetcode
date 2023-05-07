# beats 20% in time and 12% in space
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        vals = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
            return 
        dfs(root)
        sortedvals = sorted(vals)
        switch = []
        for x, y in zip(vals, sortedvals):
            if x != y:
                switch.append(x)
        count = 0
        def switching(node):
            nonlocal count
            if not node:
                return 
            if count == 2: # once we have switched twice we are done and should stop recursing
                return 
            if node.val in switch:
                for i in switch:
                    if node.val != i:
                        count += 1
                        node.val = i
                        break       # to prevent multiple switching we must break out of the loop after one switch
                        
            switching(node.left)
            switching(node.right)
            return
        switching(root)
        print(count)
            