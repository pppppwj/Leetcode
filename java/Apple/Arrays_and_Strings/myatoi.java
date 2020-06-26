package Apple.Arrays_and_Strings;
//import java.util.*
public class myatoi {
    public int atoi(String s){
        // empty test
        if (s.isEmpty()) return 0;

        // skip the space
        int i = 0;
        while(i<s.length() && s.charAt(i)==' ')
            ++i;

        
        // neg / pos 
        int sign = 1;
        if (i<s.length() && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            sign = sign - (s.charAt(i) == '-' ? 2 : 0);
            ++i;
        }

        int res=0;
        while (i<s.length() && s.charAt(i)>='0' && s.charAt(i)<='9'){
            if (res==Integer.MAX_VALUE/10 && s.charAt(i)>'7') 
                {   
                    if (sign == 1)return Integer.MAX_VALUE;
                    else return Integer.MIN_VALUE;
                }
            res = res * 10 + s.charAt(i) - '0';
            ++i;
        }
        return sign*res;
    }

    public static void main(String[] args){
        myatoi sol = new myatoi();
        String a = "  ";
        System.out.println(sol.atoi(a));
    }
}