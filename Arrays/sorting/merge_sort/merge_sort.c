#include<stdio.h>
#include<math.h>


void merge(int arr[], int p, int q, int r) {
    
}

void merge_sort(int arr[], int p, int r) {
    int q;
    if (p < r) {
        q = floor((p + r) / 2);
        merge_sort(arr, p, q);
        merge_sort(arr, q+1, r);
    }

}



int main() {
    
    return 0;
}