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
#include <limits>

class Solution {
public:

    bool valid(TreeNode* cur, long long rightBound, long long leftBound) {
        if (cur == nullptr) {
            return true;
        }

        if (!(cur->val < rightBound) || !(cur->val > leftBound)) {
            return false;
        }

        return valid(cur->left, cur->val, leftBound) && valid(cur->right, rightBound, cur->val);
    }

    bool isValidBST(TreeNode* root) {
        return valid(root, LLONG_MAX, LLONG_MIN);
    }
};
