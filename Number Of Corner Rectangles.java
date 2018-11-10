public class Solution {
    /**
     * @param grid: the grid
     * @return: the number of corner rectangles
     */
    public int countCornerRectangles(int[][] grid) {
        // Write your code here
        int res = 0;
        int row = grid.length;
        int col = grid[0].length;
        
        for (int i = 0; i < row; i++) {
            for (int j = i + 1; j < row; j++) {
                int cnt = 0;
                for (int k = 0; k < col; k++) {
                    if(grid[i][k] == 1 && grid[j][k] == 1) {
                        cnt++;
                    }
                }
                res += cnt * (cnt - 1) / 2;
            }
        }
        return res;
    }
}