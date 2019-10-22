Approach 1. Brute force. Fill each empty position with numbers to 1-9 and check if that is a valid board.

Approach 2. Backtracking

- Choice. Place a number 1-9 in the empty cell
Traverse row by row. Whenever you hit a new row, reset column to 0.

- Constraint. Sudoku rules. Only check row, coloumn, subgrid for each number placed

- Goal. Fill the complete board

nxn Sudoku is NP complete
