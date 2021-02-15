def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    end = -1
    max_substr = ""
    for (index, char) in enumerate(s):

        if char not in s[start:end+1]:

            end += 1

            if len(s[start:end+1]) > len(max_substr):
                max_substr = s[start:end+1]

        else:

            prev_index = s.index(char, start) + 1
            start = prev_index
            end = index

    print(max_substr)
    return len(max_substr)


s = input('Enter the string: ').strip()
print(lengthOfLongestSubstring(s))