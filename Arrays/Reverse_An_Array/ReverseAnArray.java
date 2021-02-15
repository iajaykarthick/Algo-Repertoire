package Arrays.Reverse_An_Array;

import java.io.*;
import java.util.*;

public class ReverseAnArray {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader()
        {
            br = new BufferedReader(
                new InputStreamReader(System.in));
        }
 
        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() { return Integer.parseInt(next()); }
 
        long nextLong() { return Long.parseLong(next()); }
 
        double nextDouble()
        {
            return Double.parseDouble(next());
        }
 
        String nextLine()
        {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
 
    public static void main(String[] args)
    {
        FastReader s = new FastReader();
        int arr[];    //declaring array
        int n = s.nextInt();
        arr = new int[n];  // allocating memory to array

        for (int i = 0; i < n; i++) {
            arr[i] = s.nextInt(); 
        }
        System.out.println(Arrays.toString(reverseAnArray(arr)));
    }

    public static int[] reverseAnArray(int[] arr){
        int end = arr.length;
        int start = -1;
        while (++start < --end){
            arr[start] = arr[start] ^ arr[end] ^ (arr[end] = arr[start]); // Swapping elements
        }
        return arr;
    }
}
