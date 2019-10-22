what if find triplets between any 2 ranges x and y?
x<a+b+c<y

What if a,b,c are allowed to be negative? Best case running time and algorithm?

Pre processing step-
Do a pass and remove all numbers from list > 2

What does this mean?
"You can assume the numbers in strings don’t overflow the primitive data type and there are no leading zeroes in numbers"

Solution-
https://stackoverflow.com/questions/19557505/triplet-whose-sum-in-range-1-2

Approach for the problem-
Suppose we create buckets A, B, C-
A=(0,2/3)
B=[2/3,1]
C=(1,2)
Then trivially there are following possibilities-
1.A, A, A
2.A, A, B
3.A, A, C
4.A, B, B
5.A, B, C
6.A, C, C
7.B, B, B
8.B, B, C
9.B, C, C
10.C, C, C

Why 10?
Find the number of integer solutions of -
x1+x2+x3=3, where each 0<=xi<=3. Should give 10. Here xi represent A/B/C. TO DO- how to solve this equation. 
