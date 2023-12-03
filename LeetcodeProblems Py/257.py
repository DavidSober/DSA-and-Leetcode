# beats 97% in time and 20% in space
# this one took a while to complete and is an "easy" problem lol

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# MAIN LOGIC EXPLANATION ================================================================================================
# main idea here is to go through dfs and record the node.val to a list path each time we go down. when we are at a leaf
# we append the node.val and the symbol '->' the question asks for to the ans list
# as we return up the tree we pop the most recent addition from path (since we do not want to double count node.vals)
# after we run the dfs helper we have populated ans list. we then must remove the extra '->' symbol that will exist at the last element
# we do this bc the question does not have a '->' for the last element in a path
# after that we join the list of list of strings into a list of strings
# we then return that as ans

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left == None and root.right == None:
            return str(root.val) 
        ans = []
        path = []
        def dfs(node):
            nonlocal ans
            nonlocal path
            if not node:
                return 
            path.append(str(node.val) + '->')
            left = dfs(node.left)
            right = dfs(node.right)
            if left == None and right == None:
                ans.append(path.copy())
            path.pop()          # if we are going up a level we remove the level we are on so as to not double count levels in path
            return node.val
        dfs(root)
        for i in range(len(ans)):
            ans[i][-1] = ans[i][-1][:-2] # trimming the last '->' at the last element by slicing the last two chars off
        print(ans)
        ret = []
        for i in range(len(ans)): 
            ret.append("".join(ans[i])) # converting list of list of strings into list of strings as q requests
        return ret 
        
