Boyer–Moore majority vote algorithms

The algorithm finds a majority element, if there is one: that is, an element that occurs repeatedly for more than half of the elements of the input. (there can be only 1 majority element)
However, if there is no majority, the algorithm will not detect that fact, and will still output one of the elements. A version of the algorithm that makes a second pass through the data can be used to verify that the element found in the first pass really is a majority.

The algorithm will not, in general, find the mode of a sequence (an element that has the most repetitions) unless the number of repetitions is large enough for the mode to be a majority. It is not possible for a streaming algorithm to find the most frequent element in less than linear space, when the number of repetitions can be small


def bm_majority(A):
    i=0
    for j in A:
        if i==0:
            m=j
            i=1
        else:
            if j==m:
                i=i+1
            else:
                i=i-1
    return m

Correctness:
If there is a majority element, the algorithm will always find it. For, supposing that the majority element is m, let c be a number defined at any step of the algorithm to be either the counter, if the stored element is m, or the negation of the counter otherwise. Then at each step in which the algorithm encounters a value equal to m, the value of c will increase by one, and at each step at which it encounters a different value, the value of c may either increase or decrease by one. If m truly is the majority, there will be more increases than decreases, and c will be positive at the end of the algorithm. But this can be true only when the final stored element is m, the majority element.


Other approaches-
brute force- O(n**2) time

sorting - O(nlogn) time

BST- store element and count in node of the BST
O(n**2) time- BST
O(nlogn) time - self balancing BST
O(n) space


* n/3 (or n/k)

Best explanation
https://cs.stackexchange.com/questions/91803/explaination-for-variation-of-boyer-moore-majority-voting-algorithm/91805#91805

Start with two empty candidate slots and two counters set to 0.
for each item:
if it is equal to either candidate, increment the corresponding count
else if there is an empty slot (i.e. a slot with count 0), put it in that slot and set the count to 1
else reduce both counters by 1


Related-
https://www.geeksforgeeks.org/majority-element/
https://www.geeksforgeeks.org/tag/moores-voting-algorithm/
https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/
https://www.geeksforgeeks.org/n3-repeated-number-array-o1-space/
