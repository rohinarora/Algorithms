Variants of problem->

Longest increasing
Longest decreasing
Longest non increasing
Longest non decreasing
Longest bitonic

Consider longest increasing

1. Brute force. Total subsequences->
O(2^n) solution. O(1) space. Make all sets possible. Each element of this set is a subsequence. Backtracking solution.

2. DP:
Solved in bottom up manner
sol1.py. O(n^2) solution. O(n) space

3. O(nlog n) solution

4. DP. top down. sol3.py. Bit similar to rod cutting (CLRS).
- non memoized right now. Can be memoized easily
- Only gives length of LIS. Haven't though about printing with top down approach

Printing the subsequence-
1. sol1.py
2. sol2.py
3. Store the LIS sequence upto element i in a list of lists (while creating solution). O(n^2) space. Poor solution. Ignore


ToDo- IB.cpp

ToDo- nlogn solution

ToDo- Print all LIS subsequences. There might be more than 1 LIS. Think of a tree being formed as you retrace back in sol1.py. Then print all paths of this tree from root to leaf

ToDo- Print the bitonic subsequence

ToDo- printing with top down approach
