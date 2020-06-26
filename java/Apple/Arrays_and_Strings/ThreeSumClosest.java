package Apple.Arrays_and_Strings;

import java.util.Arrays;

public class ThreeSumClosest {
    public int threeSumclosest(int[] nums, int target){
        Arrays.sort(nums);
        int res = nums[0]+nums[1]+nums[nums.length - 1];
        int diff = Math.abs(res - target);

        for (int i = 0; i<nums.length-2; ++i){
            int j = i+1;
            int k = nums.length-1;
            while (j<k) {
                int currsum = nums[i] + nums[j] +nums[k];
                if (currsum>target) k-=1;
                else if (currsum<target) j+=1;
                else return target;

                if (Math.abs(currsum-target)<diff) {
                    diff = Math.abs(currsum-target);
                    res = currsum;
                }
            }
        }
        return res;
    }


    public static void main(String[] args){
        int[] nums = {-1, 2, 1, -4};
        int target = 1;
        ThreeSumClosest sol = new ThreeSumClosest();
        System.out.println(sol.threeSumclosest(nums, target));
    }
}