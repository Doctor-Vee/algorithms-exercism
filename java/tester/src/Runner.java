import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Runner {

    static int colorCode(String color) {
        return Arrays.asList(colors()).indexOf(color);
    }

    static String[] colors() {
        return new String[]{"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
    }


    public static void main(String[] args) {

        System.out.println(colorCode("gryey"));
    }
}
