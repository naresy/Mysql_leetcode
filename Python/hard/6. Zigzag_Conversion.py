# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 
def convert(s: str, numRows: int) -> str:
    # Edge case handling
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a list to store each row's characters
    rows = [''] * numRows
    current_row = 0
    going_down = False

    # Iterate over each character in the input string
    for char in s:
        # Append the character to the current row
        rows[current_row] += char

        # Change direction when reaching the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        # Move up or down based on the direction
        current_row += 1 if going_down else -1

    # Concatenate all rows to get the final zigzag string
    return ''.join(rows)