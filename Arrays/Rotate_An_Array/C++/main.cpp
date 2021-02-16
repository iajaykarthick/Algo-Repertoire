#include <iostream>
#include "./RotateAnArray.cpp"

int main(){

    RotateAnArray r;
    r.getArrayFromUser();
    if ( r.getSizeOfArray() > 0 ) {
        r.getArrayRotationInputs();
        r.calc_subsets_based_on_directions();
        r.rotateArray();
        r.printArray();
    } else {
        cout << "Array size is 0. Exiting...";
    }
    return 0;
}
