#include <iostream>
using namespace std;

void reverseAnArray(int arr[], int n);
void printArray(int arr[], int n);

int main(){
    
    int n;
    cout << "Enter the size of the array: ";
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    reverseAnArray(arr, n);
    printArray(arr, n);
    return 0;
}

void reverseAnArray(int arr[], int n){
    int start = -1, end = n;
    while ( ++start < --end){
        (arr[start] ^= arr[end]), (arr[end] ^= arr[start]), (arr[start] ^= arr[end]); // Swapping elements
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " " ;
    }
}