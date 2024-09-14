# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

# solution


from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # Dictionary to store the count of characters in t
    dict_t = Counter(t)
    
    # Number of unique characters in t that must be present in the window
    required = len(dict_t)
    
    # Left and right pointer for sliding window
    left, right = 0, 0
    
    # Keep track of how many unique characters in t are present in the window
    formed = 0
    
    # Dictionary to keep track of the window's character counts
    window_counts = {}
    
    # Result: (window length, left, right)
    ans = float("inf"), None, None
    
    while right < len(s):
        # Add the current character from s into the window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # If the current character's count matches the required count in t, we consider it "formed"
        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1
        
        # Try and contract the window from the left if all required characters are present
        while left <= right and formed == required:
            char = s[left]
            
            # Update the result if this window is smaller than the previous best
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # The character at the left pointer is going to be removed from the window
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1
            
            # Move the left pointer ahead
            left += 1
        
        # Expand the window by moving the right pointer ahead
        right += 1
    
    # Return the minimum window or an empty string if no valid window was found
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Test cases
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(minWindow("a", "a"))                # Output: "a"
print(minWindow("a", "aa"))               # Output: ""
