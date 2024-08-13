#include<iostream>

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// on leetcode the official template looks like this but
// if i try to compile this locally it wont unless i change the 
// dot operator to an arrow operator.. not sure if they made a mistake here
// they probably made a mistake since trying to use this on the website will not 
// not work it will ask me to use -> funny

// int dfs(TreeNode* root) {
//     if (root == nullptr) {
//         return 0;
//     }

//     int ans = 0;
//     // do logic
//     dfs(root.left);
//     dfs(root.right);
//     return ans;
// }

int dfs(TreeNode* root) {
    if (root == nullptr) {
        return 0;
    }

    int ans = 0; // note: ans is a local var and its def is relative to
        // this current recursive function's call on the stack
    // do logic
    dfs(root->left);
    dfs(root->right);
    return ans;
}



int main() {


}