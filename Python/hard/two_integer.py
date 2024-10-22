# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

# Constraints:

# -231 <= dividend, divisor <= 231 - 1
# divisor != 0


def divide(dividend: int, divisor: int) -> int:
    # Define the range for 32-bit signed integers
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    # Edge case: If the divisor is zero, return the max int (not strictly necessary for this case as divisor != 0)
    if divisor == 0:
        return MAX_INT
    
    # Edge case: If dividend is MIN_INT and divisor is -1, return MAX_INT because the result will overflow
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT
    
    # Determine the sign of the result
    negative = (dividend < 0) != (divisor < 0)
    
    # Convert both numbers to positive
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    # The idea is to subtract divisor from dividend until dividend is smaller than divisor
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        # Increase the divisor by powers of two (bit shifts) to speed up the process
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        # Subtract the largest shifted divisor and add corresponding multiples to the quotient
        dividend -= temp_divisor
        quotient += multiple
    
    # Apply the sign to the result
    quotient = -quotient if negative else quotient
    
    # Clamp the result within the 32-bit integer range
    return max(MIN_INT, min(MAX_INT, quotient))
