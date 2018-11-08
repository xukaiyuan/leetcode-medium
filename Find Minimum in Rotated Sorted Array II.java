class Solution {
    public int findMin(int[] nums) {
        if(nums.length == 0) {
            return 0;
        }
        int start = 0;
        int end = nums.length - 1;
        int res = nums[0];
        
        while(start < end - 1) {
            int mid = (end - start) / 2 + start;
            if(nums[mid] > nums[start]) {
                res = Math.min(res, nums[start]);
                start = mid + 1;
            } else if(nums[mid] < nums[start]) {
                res = Math.min(res, nums[end]);
                end = mid;
            }
            else {
                start++;
            }
        }
        res = Math.min(res, nums[start]);
        res = Math.min(res, nums[end]);
        return res;
            
    }
}