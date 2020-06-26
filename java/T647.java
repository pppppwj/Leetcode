public class T647 {
    public int countSubstrings(String s) {
        // Method 1 ： center O(n^2)
        int count = 0;
        for (int i = 0; i < 2 * s.length() - 1; ++i) {
            int left = i / 2;
            int right = left + i % 2;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                ++count;
                --left;
                ++right;
            }
        }
        return count;
    }

    public int countSubstrings2(String s) {
        // Method 2 ： Manacher's Algorithm
        // preprocess the string (abc -> #a#b#c#)
        StringBuilder A = new StringBuilder(s);
        for (int i = s.length(); i > -1; i--)
            A.insert(i, "#");
        String s_new = A.toString();

        // create manacher array
        // apply Manacher's Algorithm
        int[] m = new int[s_new.length()];
        int center = 0;
        int r = 0;
        int i_mirror = 0;
        for (int i = 1; i < s_new.length() - 1; ++i) {
            i_mirror = 2 * center - 1;
            if (r > i)
                m[i] = Math.min(m[i_mirror], r - i);
            while (i + m[i] + 1 < s_new.length() && i - m[i] - 1 > -1
                    && s_new.charAt(i + m[i] + 1) == s_new.charAt(i - m[i] - 1))
                ++m[i];
            if (i + m[i] > r) {
                center = i;
                r = m[i];
            }
        }
        int ans = 0;
        for (int i : m)
            ans += (i + 1) / 2;
        return ans;

    }

    public static void main(String[] args) {
        T647 sol = new T647();
        String s = "aaa";
        System.out.println(sol.countSubstrings2(s));
    }
}
