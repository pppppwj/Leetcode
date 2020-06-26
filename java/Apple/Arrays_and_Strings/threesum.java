package Apple.Arrays_and_Strings;

import java.util.Map;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class threesum {

    public List<List<Integer>> tsum(int[] nums) {
        List<List<Integer>> sol = new ArrayList<>();
        Map<Integer, Integer> neg = new HashMap<>();
        Map<Integer, Integer> pos = new HashMap<>();
        int zero = 0;

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 0)
                zero += 1;
            else if (nums[i] > 0)
                pos.merge(nums[i], 1, (a, b) -> a + b);
            else
                neg.merge(nums[i], 1, (a, b) -> a + b);
        }

        if (zero >= 3)
            sol.add(Arrays.asList(0, 0, 0));

        if (zero >= 1) {
            neg.forEach((k, v) -> {
                if (pos.containsKey(-k)) sol.add(Arrays.asList(k, 0, -k));
            });
        }

        neg.forEach((k, v) -> {
            pos.forEach((pk, pv) -> {
                float f = (float) -k/2;
                if (pk<=f && pos.containsKey(-k-pk)) {
                    if (-k-pk == pk ) {if (pos.get(pk)>=2) sol.add(Arrays.asList(k,pk,pk));}
                    else sol.add(Arrays.asList(k,pk,-k-pk));
                }
            });
        });

        pos.forEach((k, v) -> {
            neg.forEach((pk, pv) -> {
                float f = (float) -k/2;
                System.out.println(f);
                if (pk<=f && neg.containsKey(-k-pk)) {
                    if (-k-pk == pk ) {if (neg.get(pk)>=2) sol.add(Arrays.asList(k,pk,pk));}
                    else sol.add(Arrays.asList(k,pk,-k-pk));
                }
            });
        });

        return sol;
    }

    public static void main(String[] args) {
        int[] nums = { 3, -2 ,-1};
        threesum sol = new threesum();
        //sol.tsum(nums)
        System.out.println(sol.tsum(nums));
        
    }
}