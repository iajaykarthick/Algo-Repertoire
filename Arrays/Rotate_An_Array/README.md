# Rotate An Array

### Pseudo code

```
num_of_rotations = 0
direction = "L" or "R" // Left or Right direction
if direction is "L"{
    Find two parts of the array such that 
    1.  first part (say A) starts from 0 to (num_of_rotations - 1)
    2.  second part (say B) starts from num_of_rotations to (arr.length - 1)
} else if direction is "R" {
    Find two parts of the array such that 
    1.  first part (say A) starts from 0 to (arr.length - num_of_rotations - 1)
    2.  second part (say B) starts from (arr.length - num_of_rotations) to (arr.length - 1)
}

reverse the first part (A) of the input array  -> we get ArB 
reverse the second part (B) of the input array -> we get ArBr
reverse the whole array -> we get BrAr which is rotated array for num_of_rotations in given direction

```


Language | Class/Function/Logic file | Wrapper file
:---: | :---: | :---:
[C++ Solution](C++/) | [RotateAnArray.cpp](C++/RotateAnArray.cpp) | [Main.cpp](C++/main.cpp)
[Java Solution](Java/) | [RotateAnArray.java](Java/RotateAnArray.java) | [Main.java](Java/Main.java)
[Python Solution](python/) | [rotateAnArray.py](python/rotateAnArray.py) | [main.py](python/main.py)
[Javascript Solution](JS/) | [RotateAnArray.js](JS/RotateAnArray.js) | [main.js](JS/main.js)
[C Solution](C/) | [RotateAnArray.C](C/RotateAnArray.C)