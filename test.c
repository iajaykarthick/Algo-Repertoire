#include <stdio.h>

void test(int n){
    int i = n;
    if (n > 0) {
        while (i > 0) {
            printf("%d ", i);
            i -= 1;
        }
        printf("\n");
        test(n-1);
    }
}

int main() {
    test(3);
    return 1;
}