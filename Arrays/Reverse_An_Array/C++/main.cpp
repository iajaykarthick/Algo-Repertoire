#include <iostream>
#include "ReverseAnArray.cpp"

using namespace std;

int main(){
    
    ReverseAnArray r;
    r.getArrayFromUser();
    r.reverseArray();
    r.printArray();
    return 0;
}