## Sum of all substrings cast as int

[Hackerrank](https://www.hackerrank.com/challenges/sam-and-substrings/problem)


Samantha and Sam are playing a numbers game. Given a number as a string, no leading zeros, determine the sum of all integer values of substrings of the string.

Given an integer as a string, sum all of its substrings cast as integers. As the number may become large, return the value modulo .

Example

Here  is a string that has  integer substrings: , , and . Their sum is , and .

Function Description

Complete the substrings function in the editor below.

substrings has the following parameter(s):

string n: the string representation of an integer
Returns

int: the sum of the integer values of all substrings in , modulo 
Input Format

A single line containing an integer as a string, without leading zeros.

Constraints

Sample Input 0

16
Sample Output 0

23
Explanation 0

The substrings of 16 are 16, 1 and 6 which sum to 23.

Sample Input 1

123
Sample Output 1

164
Explanation 1

The substrings of 123 are 1, 2, 3, 12, 23, 123 which sum to 164.