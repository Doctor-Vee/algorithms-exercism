public class Runner {

    static String twofer(String name) {
        return (name != null) ? "One for " + name + ", one for me." : "One for you, one for me.";
    }

    public static void main(String[] args) {
        System.out.println("Hello World");
        System.out.println(twofer("Victor"));
        System.out.println(twofer(null));
    }
}
