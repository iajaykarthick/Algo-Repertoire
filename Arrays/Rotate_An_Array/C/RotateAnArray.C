#include <stdio.h>

void reverseAnArray(int arr[], int start, int end);
void printArray(int arr[], int n);
void rotateAnArray(int arr[], int n);

int main(){

    int n;
    
    printf("Enter the size of array: ");
    scanf("%d", &n);

    int arr[n];

    for (int i = 0; i < n; i++) {
       scanf("%d", &arr[i]); 
    }

    rotateAnArray(arr, n);
    printArray(arr, n);
    
    return 0;
}


void reverseAnArray(int arr[], int start, int end) {

    while ( start < end ) {
        (arr[start] ^= arr[end]), (arr[end] ^= arr[start]), (arr[start] ^= arr[end]);
        start++;
        end--;
    }

}

void rotateAnArray(int arr[], int n) {

    char ch;
    int num_rotations, a_end, b_start;
    
    
    printf("Enter the number of rotations you want to make: ");
    scanf("%d", &num_rotations);
    printf("Left/Right? (L/R) ");
    scanf(" %c", &ch);
    switch (ch)
    {
    case 'L':
        a_end = num_rotations - 1;
        b_start = num_rotations;
        break;
    
    case 'R':
        a_end = n - num_rotations - 1;
        b_start = n - num_rotations;
        break;
    
    default:
        printf("Invalid option");
        return;
    }

    reverseAnArray(arr, 0, a_end);
    reverseAnArray(arr, b_start, n-1);
    reverseAnArray(arr, 0, n-1);

}

void printArray(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

}
