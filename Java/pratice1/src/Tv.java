public class Tv {
    String color;
    int channel;
    boolean power;
    static String pannel;
    void power() {
        power = !power;
    }
    void channelUp() {
        channel++;
    }
    void channelDown() {
        channel--;
    }
}
