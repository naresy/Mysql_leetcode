# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
 # Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

# solution
class Solution(object):
    def minSubArrayLen(self, target, nums):
        
        n = len(nums)
        min_len = float('inf')  # Initialize with infinity
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += nums[right]  # Expand the window by adding the current element
            
            while current_sum >= target:  # Shrink the window from the left
                min_len = min(min_len, right - left + 1)  # Update the minimum length
                current_sum -= nums[left]  # Remove the leftmost element
                left += 1
        
        return min_len if min_len != float('inf') else 0  # Return the result, or 0 if no valid subarray is found
        