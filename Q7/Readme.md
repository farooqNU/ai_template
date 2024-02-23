# Assignment 1 : Question 7
|Std ID|Name|
|I222132|Mursil Hassan|

# Screen Shot

![image](https://github.com/NUCES-Khi/assign1-7questions-mursil/assets/85949538/2b529faf-2950-49db-8317-9043951e39fa)


# Code

### Explaination 

These are the two main functions.

**isSafe(arr, row, col, n):** 
This function checks whether placing a queen at position (row, col) on the chessboard (arr) is safe or not.
It ensures that no other queen in the same column or diagonal can attack it. It iterates over the rows above the current row to check
for queens in the same column and diagonals.

**nQueen(arr, row, n):**
This is the main recursive function to solve the N-Queens problem. It tries to place queens row by row. 
If it successfully places a queen in the current row, it recursively calls itself for the next row. If all queens are successfully placed, 
it returns True. If no solution is found, it backtracks by resetting the cell and tries the next column. If all columns are tried and no 
solution is found, it returns False.

# Result 
The result is seen in the screen shot, where N Queen Probelm has been solved 

