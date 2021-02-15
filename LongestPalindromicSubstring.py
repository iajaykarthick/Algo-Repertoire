'''
Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
'''

from typing import Tuple

class Solution:
    #considering the first element as longest palindromic substring and hence marking start as 0 and max length as 1
    start = 0 
    max_length = 1

    def longestPalindrome(self, s: str) -> str:
        #Approach is to iterate over the string and consider each character as center of a possible palindromic substring 
        #and find all available palindromic substring and find longest among them

        for i in range(1, len(s)):
            # There are two thing we need to consider: 1. Even numbered palindrome 2. Odd numbered palindrome
            #Marking low as i-1 and high as i to check if the element at i is the center of any even numbered palindrome
            low = i - 1
            high = i
            self.check_if_center_of_palindrome(s, low, high)
            
            #Marking low as i-1 and high as i+1 to check if the element at i is the center of any odd numbered palindrome
            low = i - 1
            high = i + 1
            self.check_if_center_of_palindrome(s, low, high)
        print(s[self.start:self.start+self.max_length])

    def check_if_center_of_palindrome(self, s: str, low: int, high: int) -> None:
        #iterating till the both chars at low and high matches within the boundary of the string
        while low >= 0 and high < len(s) and s[low] == s[high]:
            #if the current palindrome has length greater than the length of the previously found palindromic substring, replace the start and max_length values
            if (high - low + 1) > self.max_length:
                self.start = low
                self.max_length = high - low + 1
            low -= 1
            high += 1


solution = Solution()
solution.longestPalindrome('MadaMe')

            
