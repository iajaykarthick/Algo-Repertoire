package Arrays.Rotate_An_Array.Java;

import java.util.Arrays;

import Arrays.Reverse_An_Array.Java.ReverseAnArray;
import Java_helper_classes.FastReader;

public class RotateAnArray extends ReverseAnArray {

    protected int num_rotations;
    protected String choice;

    public void getUserInputs() {

        getArrayFromUser();
        FastReader s = new FastReader();
        System.out.print("Enter the number of rotations you want to make: ");
        num_rotations = s.nextInt();
        System.out.print("Left/Right rotation (L/R) ?: ");
        choice = s.next();
    }


    public void rotateArray(){

        switch (choice.toUpperCase()) {
            case "L" :
                leftRotateAnArray(arr, num_rotations);
                break;
            case "R" :
                rightRotateAnArray(arr, num_rotations);
                break;
            default :
                System.out.println("You have entered an invalid input");
                return;
        }

    }

    public boolean isValidChoice(){
        return  choice.equalsIgnoreCase("L") || choice.equalsIgnoreCase("R");
    }

    private void leftRotateAnArray(int[] arr, int k) {
        // breaking arr into a(0 to k-1) and b(k to last) considering k as middle. reverse a and b then reverse entire to get the rotation
        reverseAnArray(0, k-1);
        reverseAnArray(k, arr.length-1);
        reverseAnArray(0, arr.length-1);
    }

    private void rightRotateAnArray(int[] arr, int k) {
        // breaking arr into a(0 to last-k) and b(k to last) considering k as middle. reverse a and b then reverse entire to get the rotation
        reverseAnArray(0, arr.length-k-1);
        reverseAnArray(arr.length-k, arr.length-1);
        reverseAnArray(0, arr.length-1);
    }

}
