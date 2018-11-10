public class Solution {
    /*
     * @param edges: a directed graph where each edge is represented by a tuple
     * @return: the number of edges
     */
    public int balanceGraph(int[][] edges) {
        // Write your code here
        HashMap<Integer, Integer> account = new HashMap<Integer, Integer>();
        for (int[] relation: edges) {
            if(account.containsKey(relation[0])) {
                account.replace(relation[0], account.get(relation[0]) - relation[2]);
            } else {
                account.put(relation[0], -relation[2]);
            }
            
            if(account.containsKey(relation[1])) {
                account.replace(relation[1], account.get(relation[1]) + relation[2]);
            } else {
                account.put(relation[1], +relation[2]);
            }
        }
        
        int cnt = 0;
        int[] remain = new int[account.size()];
        for (int value: account.values()) {
            if(value != 0) {
                remain[cnt] = value;
                cnt++;
            }
        }
        
        return helper(remain, 0, cnt, 0);
    }
    
    public int helper(int[] remain, int start, int end, int num) {
        int res = Integer.MAX_VALUE;
        while(start < end && remain[start] == 0) {
            start++;
        }
        
        for (int i = start + 1; i < end; i++) {
            if(remain[i] * remain[start] < 0) {
                remain[i] += remain[start];
                res = Math.min(res, helper(remain, start + 1, end, num + 1));
                remain[i] -= remain[start];
            }
        }
        return res == Integer.MAX_VALUE ? num: res;
    }
}