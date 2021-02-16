package Arrays.Rotate_An_Array.Java;

public class Main {
    public static void main(String[] args) {
        RotateAnArray r = new RotateAnArray();

        r.getUserInputs();
        if (r.isValidChoice()){
            r.rotateArray();
            r.printArray();
        }
    }
}
