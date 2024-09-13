# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
 # Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

# solution

class Solution(object):
    def reverseWords(self, s):
        s = list(s)
        
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the entire string
        reverse(0, len(s) - 1)
        
        n = len(s)
        start = 0
        
        # Step 2: Reverse each word in the reversed string
        for end in range(n):
            if s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1
            elif end == n - 1:
                reverse(start, end)
        
        # Step 3: Clean up spaces: remove extra spaces and manage only single spaces between words
        result = []
        i = 0
        while i < n:
            if s[i] != ' ':
                # Add word to result
                if result and result[-1] != ' ':
                    result.append(' ')
                while i < n and s[i] != ' ':
                    result.append(s[i])
                    i += 1
            else:
                i += 1
        
        return ''.join(result)

