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

    void traverseLeft(TreeNode* cur, stack<TreeNode*>& s) {
        while (cur) {
            s.push(cur);
            cur = cur->left;
        }
    }

    int kthSmallest(TreeNode* root, int k) {
        
        stack<TreeNode*> s;
        TreeNode* cur = root;

        while (k > 0) {
            traverseLeft(cur, s);
            TreeNode* nextMin = s.top();
            s.pop();
            k--;

            if (k == 0) return nextMin->val;
            
            cur = nextMin->right;
        }

    }
};
