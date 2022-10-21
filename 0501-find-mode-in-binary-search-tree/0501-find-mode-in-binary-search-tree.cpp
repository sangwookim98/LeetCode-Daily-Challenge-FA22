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
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> map;
        vector<int> result;
        int modeCount = getModeCount(root, map);
        
        for(pair<int,int> p : map) {
            if(p.second == modeCount) {
                result.push_back(p.first);
            }
        }
        
        return result;
        
    }
    
    /**
     * Traverse the tree using depth first search.
     * Return the mode count (i.e. The count of a repeated number that occurs the most.) of the tree.
     */
    int getModeCount(TreeNode* root, unordered_map<int, int> &map) {
        if(root == NULL)
            return 0;
        
        if(map.find(root->val) == map.end()) {
            map.insert(pair<int, int>(root->val, 1));
        }
        else {
            map[root->val]++;
        }
        
        return max(map[root->val], max(getModeCount(root->left, map), getModeCount(root->right, map)));
    }
};