from typing import List

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0]))) #Adding the Arrays directory (topic directory) to sys path to make use of reverse array function

from helper_files.Array import Array

class ReverseAnArray(Array):

    def reverse_an_array(self, start: int = None, end: int = None) -> List[int]:
            start = start or 0
            end = end or (len(self.arr)-1)
            while start < end:
                self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
                start += 1
                end -= 1
