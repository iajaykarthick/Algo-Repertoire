package Arrays.Reverse_An_Array.Java;

import Arrays.helper_files.Array;

public class ReverseAnArray extends Array {

    public int[] reverseAnArray(int start, int end){

        while (start < end){
            arr[start] = arr[start] ^ arr[end] ^ (arr[end] = arr[start]); // Swapping elements
            start++;
            end--;
        }
        return arr;

    }

    public int[] reverseAnArray(){
        int start = 0;
        int end = arr.length - 1;
        while (start < end){
            arr[start] = arr[start] ^ arr[end] ^ (arr[end] = arr[start]); // Swapping elements
            start++;
            end--;
        }
        return arr;

    }
}