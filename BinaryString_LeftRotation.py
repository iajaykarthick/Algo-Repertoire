'''
 a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. 
 He asked him to find all the strings generated from N left rotations one character at a time. 
 For example if S is "101", then the strings generated from left rotations will be “011”, ”110” and ”101”. 
 Out of the generated N strings, he asks the number of strings having even decimal value.

The first line consist of an integer T denoting number of test cases. 
First line of every test case consist of an integer N denoting length of the string and second line of every test cases consist of a binary string S.

'''

def rotate_left_and_count_even():
    for _ in range(int(input())):
        length = int(input())
        binary = input()
        count = 1 if binary[-1] == '0' else 0
        for i in range(length-1):
            binary = binary[1:]+binary[0]
            count += 1 if binary[-1] == '0' else 0
        print(count)

def count_zero_characters():
     for _ in range(int(input())):
        length = int(input())
        binary = input()
        print(binary.count('0'))