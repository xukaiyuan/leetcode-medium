public class Solution {
	public int findTargetSumWays(int[] nums, int S) {
		if (nums == null || nums.length == 0) {
			return 0;
		}
		return helper(nums, 0, 0, S, new HashMap<>());
	}
 
	private int helper(int[] nums, int index, int sum, 
			int S, Map<String, Integer> map) {
		// 避免数字是重复，无法找到截断点
		String encodeString = index + "->" + sum;
		if (map.containsKey(encodeString)) {
			return map.get(encodeString);
		}
		if (index == nums.length) {
			if (sum == S) {
				return 1;
			} else {
				return 0;
			}
		}
		int curNum = nums[index];
		int add = helper(nums, index + 1, sum - curNum, S, map);
		int minus = helper(nums, index + 1, sum + curNum, S, map);
		map.put(encodeString, add + minus);
		return add + minus;
	}
}

class Solution {
    private int count = 0;
    public int findTargetSumWays(int[] nums, int S) {
        calculate(nums, 0, S, 0);
        return count;
    }
    
    public void calculate(int[] nums, int i, int S, int sum) {
        if(i == nums.length) {
            if(sum == S) {
                count += 1;
            }
        } else {
            calculate(nums, i + 1, S, sum + nums[i]);
            calculate(nums, i + 1, S, sum - nums[i]);
        }
    }
}
