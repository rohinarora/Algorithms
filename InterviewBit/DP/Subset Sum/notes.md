Find subsets of array that add up to given number n.
-> we only have positive numbers
Total subsets of an array of size n- 2^n (summation nC0 to nCn).
Brute for time->
summation of (r*nCr) for r=0 to n
Reason being there will be nCr subsets of size r, and each of them will take r time to sum up r numbers. Checking the sum against constant number is O(1) time. Generate "power set" in other words. O(n*2^n) time

Backtracking- O(2^n) solution
- piggy back on power set. just add pruning/bounding function
- 2 ways to create power set. sol1.py and sol3.py
- sol2 builds on top of sol1 and sol4 builds on top of sol3. sol3 is backtracking applied to power set
- sol1- O(n*2^n) time and space.
  - O(n*2^n) time because O(2^n) leafs and O(n) time to copy to result list on average (need to make deep copy here, no just pass in pointer to list into result. insidious bug)
  - O(n*2^n) space because O(2^n) subsets are created and have length n/2 on average. Hence total space O(n*2^n)
 - https://www.youtube.com/watch?v=kyLxTdsT8ws -> based on sol1/sol2
 - sol4 has the skip duplicates trick taken from -> https://leetcode.com/problems/combination-sum-ii/discuss/16861/Java-solution-using-dfs-easy-understand
 - ToDo- apply the duplicates trick in sol2 if possible. Probably this-
 https://leetcode.com/problems/combination-sum-ii/discuss/16862/C++-backtracking-solution-with-detailed-explanation/168428
 - ToDo- DP (bottom up) solution https://leetcode.com/problems/combination-sum-ii/discuss/16916/Understanding-the-differences-between-the-DP-solution-and-simple-recursive.-Which-one-is-really-better

 DP
 - sol5.py. DP. But simpler problem. No duplicates. And return count of total subsets (not the actual values). Top down. Derived from sol2
