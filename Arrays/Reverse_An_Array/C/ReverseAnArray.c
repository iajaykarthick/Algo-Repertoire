#include <stdio.h>

void printArray();
void reverseAnArray();


int main(){

    int n;
    printf("Enter the size of array: ");
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
       scanf("%d", &arr[i]); 
    }
    reverseAnArray(arr, n);
    printArray(arr, n);
    return 0;
}

void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

}

void reverseAnArray(int arr[], int n) {

    int start = -1, end = n;
    while ( ++start < --end ) {
        (arr[start] ^= arr[end]), (arr[end] ^= arr[start]), (arr[start] ^= arr[end]);
    }

}