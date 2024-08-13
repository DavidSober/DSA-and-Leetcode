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
// note above is an ex of constructor overloading same as in java 

// dfs i made based off how i know one should do it in py
// this is not the most correct way to do it but works here
void dfs(TreeNode *node) {
    if (!node) {
        return;
    }
    
    std::cout << node->val << std::endl;
    dfs(node->left);
    dfs(node->right);

}


int main() {

    // test making a tree node with no args
    TreeNode obj1 = TreeNode();
    std::cout << obj1.val << obj1.left << obj1.right << std::endl;
    // will print 000, 
    // val = 0 ofc, left and right are null pointers which are 0 by default in cpp

    TreeNode obj2 = TreeNode(69);
    TreeNode obj3 = TreeNode(70);
    TreeNode obj4 = TreeNode(71);

    // now we will connect the nodes.
    // address of operator here since we connect pointers 
    obj1.left = &obj2;
    obj1.right = &obj3;
    obj3.left = &obj4;

    // i will add a value to the first node to make this work better
    obj1.val = 21;

    // now we have made a tree that looks like this
    /*
                 21
               /    \
              69    70
                   /
                  71
    */

   dfs(&obj1);
    // prints the following traversal which is correct
    // 21
    // 69
    // 70
    // 71

}

