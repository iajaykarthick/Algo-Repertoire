#include <iostream>
#include "../../Reverse_An_Array/C++/ReverseAnArray.cpp"

using namespace std;

class RotateAnArray : public ReverseAnArray {

    protected:
        int num_rotations;
        char choice;
        int a_end;
        int b_start;

    public:
        void getArrayRotationInputs(){
            cout << "Enter the number of rotations: ";
            cin >> num_rotations;
            cout << "Left/Right? (L/R): ";
            cin >> choice;
        }

    public:
        void calc_subsets_based_on_directions(){
            if ( choice == 'L' ) {
                a_end = num_rotations - 1;                
                b_start = num_rotations;
            } else if ( choice == 'R' ) {
                a_end = n - num_rotations - 1;
                b_start = n - num_rotations;
            }
        }


    public:
        void rotateArray(){

            reverseArray(0, a_end);
            reverseArray(b_start, n-1);
            reverseArray();

        }

};