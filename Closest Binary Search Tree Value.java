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
     * @param root: the given BST
     * @param target: the given target
     * @return: the value in the BST that is closest to the target
     */
    public int closestValue(TreeNode root, double target) {
        // write your code here
        
        double dist = Double.MAX_VALUE;
        int res = root.val;
        while(root != null) {
            double tmp = target - root.val;
            if(Math.abs(tmp) < dist) {
                res = root.val;
                dist = Math.abs(tmp);
            }
            if(tmp > 0) {
                root = root.right;
            } else {
                root = root.left;
            }
        }
        return res;
    }
}