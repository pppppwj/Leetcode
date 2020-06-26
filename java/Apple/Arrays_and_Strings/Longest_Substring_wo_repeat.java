package Apple.Arrays_and_Strings;
import java.util.Map;
import java.util.HashMap;


// // Prefix
// Integer& Integer::operator++()
// {
//     *this += 1;
//     return *this;
// }

// // Postfix
// const Integer Integer::operator++(int)
// {
//     Integer oldValue = *this;
//     ++(*this);
//     return oldValue;
// }


public class Longest_Substring_wo_repeat {
    public int lengthOfLongestSubstring(String s){
        int start = -1;
        int res = 0;
        Map<Character, Integer> aux = new HashMap<>();
        for (int i=0;i<s.length();++i){
            if (aux.containsKey(s.charAt(i)) && aux.get(s.charAt(i)) > start)
                start = aux.get(s.charAt(i));
            aux.put(s.charAt(i),i);
            res = i - start > res ? i - start : res;
        }
        return res;
    }

    public static void main(String[] args) {
        Longest_Substring_wo_repeat sol = new Longest_Substring_wo_repeat();
        String s = "abcabcbb";
        System.out.println(sol.lengthOfLongestSubstring(s));
    }
}