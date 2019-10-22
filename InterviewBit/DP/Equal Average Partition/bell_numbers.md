Bell number-
Given a set of n elements, find number of ways of partitioning it. B(n)
Ways to partition a set of n objects into k non-empty subsets and is denoted by S(n,k)-  Stirling number of the second kind
S(n+1, k) = k*S(n, k) + S(n, k-1) (recursive definition of Stirling number)
S(n,0)=0
S(0,n)=0
S(0,0)=1 (base cases)
https://www.geeksforgeeks.org/bell-numbers-number-of-ways-to-partition-a-set/
https://www.geeksforgeeks.org/count-number-of-ways-to-partition-a-set-into-k-subsets/
https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values
https://en.wikipedia.org/wiki/Bell_number  
Ways to partition set of n numbers into 2 non empty sets- S(n,2)
S(n,2)=O(n\**2)
Hence, brute force time is O(n\**2). Simply create O(n\**2) partitions and check each partitions' average in O(1) time
How to do brute force and create all partitions possible?. ToDo

Computing bell numbers-
1. Compute S(n, k) for k = 1 to n
2. Use Bell Triangle . bell.py. O(n^2) time. O(n^2) space.
3. More efficient method of computing Bell Numbers. ToDo

Computing Sterling numbers of second kind-
1. S(n, k) = k*S(n-1, k) + S(n-1, k-1). sterling.py. Can be memoized easily
https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values

ToDo-
Another problem that can be solved by Bell Numbers.
A number is squarefree if it is not divisible by a perfect square other than 1. For example, 6 is a square free number but 12 is not as it is divisible by 4.
Given a squarefree number x, find the number of different multiplicative partitions of x. The number of multiplicative partitions is Bell(n) where n is number of prime factors of x. For example x = 30, there are 3 prime factors of 2, 3 and 5. So the answer is Bell(3) which is 5. The 5 partitions are 1 x 30, 2 x15, 3 x 10, 5 x 6 and 2 x 3 x 5.
Exercise:
The above implementation causes arithmetic overflow for slightly larger values of n. Extend the above program so that results are computed under modulo 1000000007 to avoid overflows.


Variants-
partitions which have equal sum?
partitions which have equal product?
