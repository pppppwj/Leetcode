package Apple.Arrays_and_Strings;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
public class Two_Sum {
    // brute force
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; ++i) {
            for (int j = i + 1; j < nums.length; ++j)
                if (nums[i] + nums[j] == target)
                    return new int[] { i, j };
        }
        return new int[] {};
    }

    public int[] TwoSum2(int[] nums, int target) {
            Map<Integer, Integer> res = new HashMap<>();
            for (int i=0;i<nums.length;++i){
                if (res.containsKey(nums[i])) return new int[] {i,res.get(nums[i])};
            
                res.put(target-nums[i],i);
            }
            return new int[] {};
            
    }

    public static void main(String[] args) {
        Two_Sum sol = new Two_Sum();
        // test case
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        System.out.println(Arrays.toString(sol.TwoSum2(nums, target)));
    }
}//