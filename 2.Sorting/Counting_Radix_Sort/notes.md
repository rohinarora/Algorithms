* Counting sort uses space of $\theta(k+n)$
* Counting sort uses time of $\theta(k+n)$
* CLRS Pg 195
  * Array C starts from 0. Very likely coz of line 7 in pseudocode.
  * A and B start from n
  * len(C)=k
  * len(A)=len(B)=n
  * A- original input
  * B- output
* Counting sort is "stable sort"
  * Preserves relative order of equal elements
* Which of previous sorting algos were stable sorts?
  * Some Sorting Algorithms are stable by nature, such as Bubble Sort, Insertion Sort, Merge Sort, Count Sort etc.
  * Quick Sort, Heap Sort etc. are unable, but can be made stable
  * https://www.geeksforgeeks.org/stability-in-sorting-algorithms/
* Radix sort
  * We call counting sort on digits starting from LSB
  * Example
  * Proof of correctness-
    * We call counting sort, and counting sort preserves the order
  * When we call on digits, k=10 (0-9)
  * pseudocode CLRS Pg 198
