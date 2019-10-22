linear/sequential data structures -
array, linked list, stack, queue

choice of data structure depends on-
what needs to be stored
space required
cost of operating on the data structure


Tree:
tree with n nodes has exactly n-1 edges. All nodes except root have 1 incoming edge

Depth of node x= length of path from root to node x

Height of x= length of longest from x to a leaf

Height of leaf nodes=0

Height of tree= height of root node

define root node has level 0. then
max nodes at level i -> pow(2,i)

Consider perfect binary tree with k levels. number of nodes=pow(2,k+1)-1=n. Solve for n/k interchangeably

height of complete binary tree: floor(log2(n)) where n nodes in tree

Operations on tree depend on height of trees. So its good to have trees with small height. On the other hand sparse trees are tall and take longer time on basic operations.

height of tree with only 1 node- 0
height of tree with 0 nodes- -1

Implement graph and tree from scratch

Binary tree can be implemented as -
1. dynamically created nodes
2. array
