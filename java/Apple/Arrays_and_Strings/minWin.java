package Apple.Arrays_and_Strings;
import java.util.Map;
import java.util.HashMap;


public class minWin {

    public String MinWin(String s, String t){
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        int missing = t.length();
        // init map 
        for (int i = 0;i<t.length();++i){
            //int count = map.getOrDefault(s.charAt(i), 0);
            map.put(t.charAt(i),map.getOrDefault(t.charAt(i), 0)+1);
        }

        int start = 0, end = 0;
        int i=0, j=0;

        while (end < s.length()){
            if (map.getOrDefault(s.charAt(end), 0)>0) --missing;
            //int count = map.getOrDefault(s.charAt(end), 0);
            map.put(s.charAt(end),map.getOrDefault(s.charAt(end), 0)-1);

            ++end;

            if (missing==0){
                while(map.get(s.charAt(start))<0) {
                    map.put(s.charAt(start),map.get(s.charAt(start))+1);
                    ++start;
                }
                map.put(s.charAt(start),map.get(s.charAt(start))+1);
                ++missing;

                if (j==0 || end - start < j - i){
                    j=end;
                    i=start;
                }
                ++start;
            }
        }
        return s.substring(i,j);


    }



    public static void main(String[] args){
        String s = "ADOBECODEBANC", t = "ABC";
        minWin sol = new minWin();
        System.out.println(sol.MinWin(s, t));
    }
}