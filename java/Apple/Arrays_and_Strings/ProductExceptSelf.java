package Apple.Arrays_and_Strings;
import java.util.Arrays;


public class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums){
        int[] sol = new int[nums.length];
        Arrays.fill(sol,1);
        int l = 1;
        for (int i=1;i<nums.length;++i){
            l*=nums[i-1];
            sol[i]*=l;
        }
        int r=1;
        for (int i=nums.length-2;i>-1;--i){
            r*=nums[i+1];
            sol[i]*=r;
        }

        return sol;
    }
    public static void main(String[] args){
        int[] nums = {1,2,3,4};
        ProductExceptSelf sol = new ProductExceptSelf();
        System.out.println(Arrays.toString(sol.productExceptSelf(nums)));
    }
}