Approaches to the problem-
1. Mark visited nodes.
- Change the val attribute to some MINVAL. Not a safe solution. What if some node already had MINVAL in the val attribute. Not ideal solution. Should be easy to implement
- Implicitly mark visited nodes by storing the nodes visited (their objects/addresses) in a set. Set lookup is O(1) time. sol1 is based on this. How to find length of linked list if there is a loop present ? We can count the number of distinct nodes in a cyclic linked list using the above Hash solution.
- Create a temp node, and point the next field of each node visited to this temp node. If you come across a node which points to this temp node, cycle exists. LL is destroyed in this case. sol2.py is based on this.
- Floyd’s Cycle-Finding Algorithm. sol3.py
https://stackoverflow.com/a/6110767
https://www.youtube.com/watch?v=LUm2ABqAs1w
variants- remove loop from LL, find length of LL with loop, etc. To remove loop, mark the node just before cycle completion as none
