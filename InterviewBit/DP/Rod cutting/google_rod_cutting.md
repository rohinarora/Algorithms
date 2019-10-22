IB rod problem

- Why won't greedy work here? Or what would be incorrect greedy approach here?
- Lets say there are M cuts to be made. The brute force way here is checking M! possibilities and picking the min cost.
- Let’s say from the set of cuts A1, A2, …, AN, first cut you make at is Ai.
Then, we have to make cuts from set A1, A2, …, Ai-1, whose order doesn’t depend on set of cuts Ai+1, Ai+2, …, AN. These are 2 subproblems whose solution can be combined to get optimal solution for original subproblem

Problem- dp(i, j)
We define dp(i, j) as minimum cost for making cuts Ai, Ai+1, …, Aj


Brute force. Given a sequence, N! combinations possible.

Based on MCP
https://codeforces.com/blog/entry/61525


https://www.youtube.com/watch?v=IRwVmTmN6go
https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/
https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
https://www.youtube.com/watch?v=vgLJZMUfnsU
https://www.youtube.com/watch?v=zFe-SX7jzDs
