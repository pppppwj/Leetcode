import java.util.Arrays;
import java.util.Stack;

public class T739 {
    public int[] dailyTemperatures(int[] T) {
        int[] ans = new int[T.length];
        Stack<Integer> stack = new Stack<Integer>();
        for (int i = T.length - 1; i >= 0; --i) {
            while (!stack.isEmpty() && T[i] >= T[stack.peek()]) {
                stack.pop();
            }
            ans[i] = stack.isEmpty() ? 0 : stack.peek() - i;
            stack.push(i);
        }
        return ans;
    }

    public static void main(String[] args) {
        T739 solution = new T739();
        int[] test = { 89, 62, 70, 58, 47, 47, 46, 76, 100, 70 };
        System.out.println(Arrays.toString(solution.dailyTemperatures(test)));
    }
}
