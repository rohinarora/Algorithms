### Notes
* in_order_traversal- 3 ways
  * recursive (1)
  * iterative and stack (2)
  * iterative and 2 pointers (morris traversal) (3)
* pre order traversal
  * recursive (simple modification of 1)
  * iterative and stack (simple modification of 2)
  * iterative and 2 pointers (morris traversal) (simple modification of 3)
* post_order_traversal
  * recursive (simple modification of 1)
  * iterative and 1 stack (some modification of 2)
  * iterative and 2 stacks
  * morris?
* calling in_order_traversal prints BST in sorted order (O(n) time.)
  * We spent O(nlogn) time to build the tree
* Morris pre/inorder- O(1) space, O(n) time
  * Idea of Morris Traversal is based on Threaded Binary Tree.
* Tree search
  * recursive
  * iterative
* Tree Min, Tree Max
* Successor, Predecessor
  * refer pred_succ_bst.md
* Tree insert
  * trailing pointer
* Tree delete (and Transplant)
  * refer delete.md

### Code 🐍
* [Traversals](https://github.com/rohinarora/Algorithms/blob/master/Trees/Binary%20Search%20Trees/CLRS_Ch12/BST_traveral.py)
* [Insert](https://github.com/rohinarora/Algorithms/blob/master/Trees/Binary%20Search%20Trees/CLRS_Ch12/bst.py)
* [Rank](https://github.com/rohinarora/Algorithms/blob/master/Trees/Binary%20Search%20Trees/CLRS_Ch12/bstsize.py)

### To Do
* [BFS tree print](https://www.geeksforgeeks.org/level-order-tree-traversal/)
* [Use post order traversal to delete a tree](https://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/)
* Related to postorder traveral [RPN](https://en.wikipedia.org/wiki/Reverse_Polish_notation)


### Meta
pip install binarytree
