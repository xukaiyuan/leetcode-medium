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
import java.util.PriorityQueue;
public class Solution {
    /**
     * @param root: the given BST
     * @param target: the given target
     * @param k: the given k
     * @return: k values in the BST that are closest to the target
     */
    private List<Integer> res = new ArrayList<Integer>();
    private Comparator<double[]> compare = new Comparator<double[]>() {
        public int compare(double[] a, double[] b) {
            if(a[0] > b[0]) {
                return 1;
            } else if(a[0] < b[0]) {
                return -1;
            } else {
                return 0;
            }
        }
    };
    private PriorityQueue<double[]> pq = new PriorityQueue<double[]>(compare);
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        // write your code here
        inOrder(root, target);
        for (int i = 0; i < k; i++) {
            double[] cur = pq.poll();
            res.add((int)cur[1]);
        }
        return res;
    }
    
    public void inOrder(TreeNode root, double target) {
        if(root == null) {
            return;
        }
        inOrder(root.left, target);
        double dist = Math.abs(target - root.val);
        pq.offer(new double[] {dist, (double)root.val});
        inOrder(root.right, target);
    }
}