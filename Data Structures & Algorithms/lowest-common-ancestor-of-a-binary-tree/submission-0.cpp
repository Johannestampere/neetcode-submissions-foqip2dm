/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr || root->val == p->val || root->val == q->val) {
            return root;
        }

        TreeNode* leftRes = lowestCommonAncestor(root->left, p, q);
        TreeNode* rightRes = lowestCommonAncestor(root->right, p, q);

        if (leftRes != nullptr && rightRes != nullptr) {
            return root;
        }

        if (leftRes == nullptr && rightRes != nullptr) {
            return rightRes;
        }

        else {
            return leftRes;
        }

    }
};