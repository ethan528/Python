public class Main {
    public static void main(String[] args) {
        Tv tv1 = new Tv();
        Tv tv2 = new Tv();
        System.out.println(Tv.pannel);
        tv1.color = "red";
        tv1.channelUp();
        System.out.println(tv1.channel);
    }
}