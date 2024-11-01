# BFS sol
# apparently I was supposed to use dfs but this still worked
# overall description. 
# bfs through bin tree and create a cousion list 
# we do this by looking at the children nodes grouping them by their parent
# for each node in the current level.
# then we calculate the level sum aka the sum of all vals for the curr level
# then we go through the cuz list and get the val of the curr siblings
# then we take the diff between that and the level sum to get the replacement val 
# for the current siblings. 
# lastly we account for the first 3 levels always being 0 val  
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        curr_level = 0
        while queue:
            curr_len = len(queue)
            
            cuz_lst = []
            for node in queue:
                child_lst = []
                if node.left:
                    child_lst.append(node.left)
                if node.right:
                    child_lst.append(node.right)
                if child_lst:
                    cuz_lst.append(child_lst[:])
            if not cuz_lst:
                break
            if len(cuz_lst) > 1:
                # total sum of vals
                # diff between that and siblings vals is ans
                level_sum = 0 
                for siblings in cuz_lst:
                    for sib in siblings:
                        level_sum += sib.val
                for siblings in cuz_lst:
                    curr_siblings_vals = 0
                    for sib in siblings:
                        curr_siblings_vals += sib.val
                    delta = level_sum - curr_siblings_vals
                    for sib in siblings:
                        sib.val = delta
            elif len(cuz_lst) <= 1:
                for siblings in cuz_lst:
                    for sib in siblings:
                        sib.val = 0
            
            for _ in range(curr_len):
                curr = queue.popleft()
                if curr_level < 2:
                    curr.val = 0
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            curr_level += 1
        return root