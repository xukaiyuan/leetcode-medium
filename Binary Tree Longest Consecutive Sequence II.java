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
    public int longestConsecutive2(TreeNode root) {
        // write your code here
        helper(root, root);
        return res;
    }
    public int[] helper(TreeNode cur, TreeNode parent) {
        if(cur == null) {
            return new int[] {0, 0};
        }
        int[] left = helper(cur.left, cur);
        int[] right = helper(cur.right, cur);
        
        res = Math.max(left[0] + right[1] + 1, res);
        res = Math.max(left[1] + right[0] + 1, res);
        
        int incr= 0;
        int desc = 0;
        if(cur.val == parent.val + 1) {
            incr = Math.max(left[0], right[0]) + 1;
        } else if(cur.val == parent.val - 1) {
            desc = Math.max(left[1], right[1]) + 1;
        }
        return new int[] {incr, desc};
    }
}