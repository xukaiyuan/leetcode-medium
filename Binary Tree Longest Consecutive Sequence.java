/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the root of binary tree
     * @return: the length of the longest consecutive sequence path
     */
    private int res = 0;
    public int longestConsecutive(TreeNode root) {
        // write your code here
        if(root == null) {
            return 0;
        }
        traversal(root, 0, root.val);
        return res;
    }
    
    public void traversal(TreeNode root, int cur, int val) {
        if(root == null) {
            return;
        }
        if(root.val == val + 1) {
            cur++;
        } else {
            cur = 1;
        }
        res = Math.max(res, cur);
        traversal(root.left, cur, root.val);
        traversal(root.right, cur, root.val);
    }
}