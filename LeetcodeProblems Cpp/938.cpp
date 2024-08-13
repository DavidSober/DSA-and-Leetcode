/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0; // i made ans global so i can easily update it in the 
    // recursive calls

    int dfs(TreeNode *node, int low, int high) {
        if (node == nullptr) {
            return 0;
        }

        if (node->val <= high && node->val >= low) {
            std::cout << node->val << std::endl;
            ans += node->val;
        }
        dfs(node->left, low, high);
        dfs(node->right, low, high);
        return ans;
    }
    
    int rangeSumBST(TreeNode* root, int low, int high) {
        
        return dfs(root, low, high);
    }
};