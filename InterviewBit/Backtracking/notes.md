Start with "Factorial" and "Fibonacci" DIR

Recursive vs Iterative-
https://www.codeproject.com/Articles/21194/Iterative-vs-Recursive-Approaches

DP is used when optimization problems exists.

Backtracking is used when you need to explore all possible solutions (And maybe prune based on some criterion. Or not). Recursion is fundamental to backtracking. Bounding function prunes the tree, saves run time (based on problem)

Backtracking is DFS kind of exploration. Tree is generated and we keep hitting the roots and coming back (via recursion)
Branch and bound is BFS kind of exploration. Tree is generated level wise.

N queen problem.
Can place in 16C4 ways. Naive
Constraint. Place each queen only in 1 row. So 4 choices for each queen. 4^4 ways.
Constraint. Place only 1 queen in 1 column. 4! ways left.



It is recommended to master recursion before jumping on to backtracking. Especially those problems of recursion that do not have a recursive formula given.
Examples - Print digits of a number in reverse order using Recursion.  Write Recursive function that tells if a given string is palindrome or not.  A Recursive function of binary search.
Then gradually move to little complex problems - Solving a SuDoKu puzzle using recursion.  Given a 2D array (MAZE) - Print path to go from one end to another.  Given a matrix of alphabets -  Find a given word.
By the end of above listed problems - BackTracking would be under your control.

Start with the definition in wikipedia. Then try to understand some classic backtracking problems like n-queen. Try to compare it with other algorithms and figure when to apply or not



In some contexts, we have no choice but to exhaustively examine all possibilities, such as when
trying to find some globally optimal result, But what if we are interested in finding any solution,
whichever one that works out first? At each decision point, we can choose one of the available
options, and sally forth, hoping it works out. If we eventually reach our goal from here, we're
happy and have no need to consider the paths not taken. However, if this choice didn't work out
and eventually leads to nothing but dead ends; when we backtrack to this decision point, we try
one of the other alternatives.


What’s interesting about backtracking is that we back up only as far as needed to reach a
previous decision point with an as-yet-unexplored alternative. In general, that will be at the most
recent decision point. Eventually, more and more of these decision points will have been fully
explored, and we will have to backtrack further and further. If we backtrack all the way to our
initial state and have explored all alternatives from there, we can conclude the particular problem
is unsolvable. In such a case, we will have done all the work of the exhaustive recursion and
known that there is no viable solution possible



Backtracking- Tree pruning.




The total number of nodes explored in state space tree gives the total number of recursive calls done in backtracking.

permute and subset problem- both have depth of tree N. We have N decisions to make. Depth of tree represents decisions to be made. Branching at each node tells choices at each step. Always 2 for subset subset problem. len(rest) in permute problem (goes from N at root to 1 at bottom)


https://www.geeksforgeeks.org/print-palindromic-permutations-given-string-alphabetic-order/

General approach-
https://leetcode.com/problems/palindrome-partitioning/discuss/182307/Java%3A-Backtracking-Template-General-Approach
