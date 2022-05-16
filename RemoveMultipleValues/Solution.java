import java.util.ArrayList;

public class Solution {
    public static int[] solution(int[] data, int n) {
        // Your code here
        ArrayList<Integer> outputArrayList = new ArrayList<Integer>();
        for (int i : data) {
            int amount = 0;
            for (int j : data) {
                if (i == j) {
                    amount++;
                }
            }
            if (amount <= n) {
                outputArrayList.add(i);
            }
        }
        int[] output = new int[outputArrayList.size()];
        for (int i = 0; i < outputArrayList.size(); i++) {
            output[i] = outputArrayList.get(i);
        }
        return output;
    }
}
