-- Given a string s, find the length of the longest 
-- substring
--  without repeating characters.

 

-- Example 1:

-- Input: s = "abcabcbb"
-- Output: 3
-- Explanation: The answer is "abc", with the length of 3.
-- Example 2:

-- Input: s = "bbbbb"
-- Output: 1
-- Explanation: The answer is "b", with the length of 1.
-- Example 3:

-- Input: s = "pwwkew"
-- Output: 3
-- Explanation: The answer is "wke", with the length of 3.
-- Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

-- Constraints:

-- 0 <= s.length <= 5 * 104
-- s consists of English letters, digits, symbols and spaces.
--solution
def length_of_longest_substring(s: str) -> int:
    char_set = set()  # Set to store characters in the current window
    left = 0  # Left pointer of the sliding window
    max_len = 0  # Variable to track the maximum length

    # Iterate with the right pointer over the string
    for right in range(len(s)):
        # If the character at right pointer is a duplicate, move left pointer
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove the character at left pointer
            left += 1  # Move the left pointer to the right

        char_set.add(s[right])  # Add the character at the right pointer to the set
        max_len = max(max_len, right - left + 1)  # Update the maximum length

    return max_len
