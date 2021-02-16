import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(sys.path[0]))) #Adding the root directory (topic directory) to sys path to make use of reverse array function

from Reverse_An_Array.python.reverseAnArray import ReverseAnArray


class RotateAnArray(ReverseAnArray):

    num_rotations = 0
    choice = ''
    a_end = None
    b_start = None

    def get_user_input(self):
        super().get_user_input()
        self.num_rotations = int(input('Enter the number of rotations you want to make: '))

    def calc_subset_based_on_direction(self):        
        if input('Left or Right ? (L/R): ').upper() == 'L':
            self.a_end = self.num_rotations -1
            self.b_start = self.num_rotations
        else:
            self.a_end = len(self.arr) - self.num_rotations - 1
            self.b_start = len(self.arr) - self.num_rotations


    def rotate_array(self):
        super().reverse_an_array(0, self.a_end)
        super().reverse_an_array(self.b_start, len(self.arr)-1)
        super().reverse_an_array()
        

