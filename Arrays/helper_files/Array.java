package Arrays.helper_files;

import java.util.Arrays;

import Java_helper_classes.FastReader;

public class Array {
    
    int n; 
    protected int[] arr; //declaring array

    public void getArrayFromUser(){
        FastReader s = new FastReader();
        System.out.println("Enter the size of array: ");
        n = s.nextInt();
        arr = new int[n];  // allocating memory to array
        System.out.println("Enter the elements of array: ");
        for (int i = 0; i < n; i++) {
            arr[i] = s.nextInt(); 
        }
    }

    public void printArray(){
        
        System.out.println(Arrays.toString(arr));

    }



}
