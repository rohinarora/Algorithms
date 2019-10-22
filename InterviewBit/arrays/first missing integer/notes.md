

* Not clear-
We can also use hashing. We can build a hash table of all positive elements in the given array.
Once the hash table is built, all positive integers, starting from 1 can be searched here. As soon as we find a number which is not there in the hash table, we return it
Approximately, this approach may take O(n) time, but it requires O(n) extra space.
* Guess:
Create a hash table. Searching in hash table is O(1) time. We need to search only O(n) times in worst case (for numbers 1-N)


* Good insight
Note that ( N being the size of the array ), A[i]<=0 and A[i]>N are not the numbers you are looking for because the missing positive integer will be in the range [1, N+1].
The answer will be N+1 only if all of the elements of the array are exact one occurrence of [1, N].

* Another insight
If using extra space was an option, creating buckets would have been an easy solution.
Creating an array of size N initialized to 0, for every value A[i] which lies in the range [1, N], we would have incremented its count in the array. Consequently, we would traverse the array to find the first array position with value 0, hence finding our answer.
However, since we are not allowed buckets, can we use the existing array as bucket somehow?

* Implementation
 We use array elements as index. To mark presence of an element x, we change the value at the index x to negative. But this approach doesn’t work if there are non-positive (-ve and 0) numbers. So we segregate positive from negative numbers as first step and then apply the approach.
