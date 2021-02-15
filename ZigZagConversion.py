'''
Zig Zag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
'''

def convert(s: str, numRows: int) -> str:

    #if numRows is one, returning the string as it is
    if numRows == 1:
        return s

    #Creating numRows sized array of empty string to store the zig zag pattern of the given string
    arr_str = ["" for n in range(numRows)]
    
    #initializing down variable; it will be 1 if direction is down and 0, if direction is up
    down = 1
    index = 0
    for char in s:
        if index >= 0 and index < len(arr_str):
            arr_str[index] += char
            if index == 0:
                down = 1
            elif index == len(arr_str) - 1:
                down = 0
        if down:
            index += 1
        else:
            index -= 1
    return ''.join(arr_str)

convert('PAYPALISHIRING', 3)