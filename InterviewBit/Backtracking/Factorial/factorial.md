f(n)= n!
    = n* (n-1)!
    = n*f(n-1) if n>0
    = 1        if n=0 (base case)

T(n)=T(n-1)+c
    =T(0) + n*c

T(0)=1

T(n)=O(n)
