import java.util.ArrayList;
import java.util.List;

public class Saved {

    static int countBalancingElements(List<Integer> arr) {
        List<Integer> tempArray;
        Integer sumEven;
        Integer sumOdd;
        Integer n = 0;
        for (int i = 0; i < arr.size(); i++) {
            tempArray = new ArrayList<>(arr);
            tempArray.remove(i);
            sumEven = 0;
            sumOdd = 0;

            for (int k = 0; k < tempArray.size(); k++) {
                if (k % 2 == 0) {
                    sumEven += tempArray.get(k);
                } else {
                    sumOdd += tempArray.get(k);
                }
            }
            if (sumEven == sumOdd) n++;
        }
        return n;
    }
}
