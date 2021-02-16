#include <iostream>
#include "../../helper_files/Array.cpp"

using namespace std;

class ReverseAnArray : public Array{

    public:
        void reverseArray(){
            int start = -1, end = n;
            while ( ++start < --end){
                (arr[start] ^= arr[end]), (arr[end] ^= arr[start]), (arr[start] ^= arr[end]); // Swapping elements
            }
        }

    public:
        void reverseArray(int start, int end){
            while ( start < end){
                (arr[start] ^= arr[end]), (arr[end] ^= arr[start]), (arr[start] ^= arr[end]); // Swapping elements
                start++;
                end--;
            }
        }

};