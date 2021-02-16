#include <iostream>
using namespace std;

class Array {

    protected:
        int n;
        int *arr = new int[n];
        
    public:
        void getArrayFromUser(){
            cout << "Enter the size of the array: ";
            cin >> n;
            for (int i = 0; i < n; i++) {
                cin >> arr[i];
            }
        }

    public:
        void printArray() {
            for (int i = 0; i < n; i++) {
                cout << arr[i] << " " ;
            }
        }

      public:
        int getSizeOfArray(){
            return n;
        }

};