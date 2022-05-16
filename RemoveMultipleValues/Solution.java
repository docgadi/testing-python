import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public static int[] solution(int[] data, int n) {
        // Your code here
        ArrayList<Integer> dataArrayList = new ArrayList<Integer>();
        ArrayList<Integer> removeNums = new ArrayList<Integer>();
        for (int i : data) {
            dataArrayList.add(i);
        }
        for (int i = 0; i < dataArrayList.size(); i++) {
            int amount = 0;
            for (int j = 0; j < dataArrayList.size(); j++) {
                if (dataArrayList.get(j).equals(dataArrayList.get(i))) {
                    amount++;
                }
            }
            if (amount > n) {
                removeNums.add(dataArrayList.get(i));
            }
        }
        for (int i = 0; i < removeNums.size(); i++) {
            for (int j = 0; j < dataArrayList.size(); j++) {
                if (dataArrayList.get(j).equals(removeNums.get(i))) {
                    dataArrayList.remove(j);
                    break;
                }
            }
        }
        int[] output = new int[dataArrayList.size()];
        for (int i = 0; i < dataArrayList.size(); i++) {
            output[i] = dataArrayList.get(i);
        }
        return output;
    }
}
