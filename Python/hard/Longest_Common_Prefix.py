# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the longest common prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the array
    for string in strs[1:]:
        # Reduce the prefix length until it matches the start of the string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Example usage:
print(longest_common_prefix(["flower","flow","flight"]))  # Output: "fl"
print(longest_common_prefix(["dog","racecar","car"]))    # Output: ""
