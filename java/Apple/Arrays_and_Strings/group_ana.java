package Apple.Arrays_and_Strings;

//import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;


public class group_ana {

    public static String str2Arrays(String s){
        int[] res = new int[26];
        for (int i = 0;i<s.length();++i){
            res[s.charAt(i)-'a']+=1;
        }
        StringBuilder sb = new StringBuilder("");
        for (int i=0;i<res.length;i++){
            sb.append(res[i]);
            sb.append("#");
        }
        return sb.toString();
    }


    public List<List<String>> Group_Anagrams(String[] strs){
        Map<String, List> ans = new HashMap<String, List>();
        for (String s: strs){
            String temp = str2Arrays(s);
            if (!ans.containsKey(temp)) ans.put(temp, new ArrayList<String>());
            ans.get(temp).add(s);
        }
        return new ArrayList(ans.values());
    }



    public static void main(String[] args){
        group_ana sol = new group_ana();
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(sol.Group_Anagrams(strs));
    }

}