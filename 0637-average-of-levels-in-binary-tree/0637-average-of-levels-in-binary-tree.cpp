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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        queue<TreeNode*> nodes;
        nodes.push(root);
        while(!nodes.empty()) {
            long temp=0;
            int s=nodes.size();
            for(int i=0; i<s; i++) {
                TreeNode* t = nodes.front();
                nodes.pop();
                if(t->left) nodes.push(t->left);
                if(t->right) nodes.push(t->right);
                temp+=t->val;
            }
            result.push_back((double)temp/s);
        }
        return result;        
    }
};